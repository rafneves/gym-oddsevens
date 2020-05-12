import gym
from gym import spaces
from gym.utils import seeding
import numpy as np
    
class OddsEvensAdversarialHardEnv(gym.Env):
    """
    Description:
        Two competitors (agent and environment) play Odds and Evens. The goal is to win from the environment as many as it is possible.
    Observation: 
        Type: MultiBinary(2)
        Num	Observation                                                Values
        0	The sum result that will make Environment win       0 (Evens) or 1 (Odds)
        1	Number played by Environment in the last step       0 (Evens) or 1 (Odds)
        
    Actions:
        Type: Discrete(2)
        Num	Action
        0	Play 'Evens'
        1	Play 'Odds'
        
    Reward:
        Reward is 1 for every step which the agent wins, 0 if it looses.
    """
    
    metadata = {
        'alpha': 0.8,
        'beta' : 0.5,
        'adversarial': True
    }
    
    agentmoves = []
    
    def __init__(self):
        self.action_space = gym.spaces.discrete.Discrete(2)
        self.observation_space = gym.spaces.MultiBinary(2)
       
        # Probability of playing "Evens"
        self.current_alpha = self.metadata['alpha']
        
        # Probability of environment choose that the "Evens" will make it win.
        self.beta = self.metadata['beta']
        self.adversarial = self.metadata['adversarial']
        
        # Clean data structures
        self.chosen = None
        self.seed()
        
    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def _updatealpha(self):
        # We will estimate the probability of the agent choose "Evens" with the average
        # mean until now. Further, we will choose alpha based on the best response of
        # a rational agent considering the "Evens and Odds" non-cooperative games with
        # payoffs being 0 or 1.
        
        agents_alpha_estimate = np.mean(self.agentmoves)
        
	# Old rule
        agents_move_estimate = int(agents_alpha_estimate < 0.5)
        
        
        new_alpha = int(((self.chosen == 0) and (agents_move_estimate == 1)) or
                        ((self.chosen == 1) and (agents_move_estimate == 0))) 
        
        return (new_alpha)
        
    def step(self, action):
        assert self.action_space.contains(action), "%r (%s) invalid"%(action, type(action))

        # Initialization
        obs = None
        reward = None
        done = False
        
        # It is time to environtment to play. Choose a number {0,1}.        
        draw = self.np_random.binomial(1, 1 - self.current_alpha, 1)
        
        matchsum = action + draw
        
        # Environment of when environment wins.
        envwins = (matchsum % 2 == self.chosen) 
        
        reward = int(not envwins)
        
        self.chosen = self._choose()
        obs = np.append(self.chosen, draw)
        
        if self.adversarial == True:
            # Update alpha for the next step. Environment only uses the last matches.
            if len(self.agentmoves) > 0:
                self.current_alpha = self._updatealpha()
            
            # Record the agent move.
            self.agentmoves.append(action)
            
        return obs, reward, done, {}

    def _choose(self):    
        chosen = self.np_random.binomial(1, 1 - self.beta, 1)
        return (chosen)
    
    def reset(self):
        self.current_alpha = self.metadata['alpha']
        self.chosen = self._choose()

        self.agentmoves = []
  
        return np.append(self.chosen, 0)
    
    def render(self, mode=None):
        pass
    
    
    def close(self):
        pass

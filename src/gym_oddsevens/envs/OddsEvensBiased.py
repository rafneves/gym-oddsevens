import gym
from gym import spaces
from gym.utils import seeding
import numpy as np
    
class OddsEvensBiasedEnv(gym.Env):
    """
    Description:
        Two competitors (agent and environment) play Odds and Evens. The goal is to win from the environment as many matches as it is possible.
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
        'beta' : 0.5
    }
        
    def __init__(self):
        self.action_space = gym.spaces.discrete.Discrete(2)
        self.observation_space = gym.spaces.MultiBinary(2)
       
        # Probability of playing "Evens"
        self.alpha = self.metadata['alpha']
        
        # Probability of environment defining that "Evens" will win the match.
        self.beta = self.metadata['beta']

        self.chosen = None
        self.seed()
        
    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    
    def step(self, action):
        assert self.action_space.contains(action), "%r (%s) invalid"%(action, type(action))

        # Initialization
        obs = None
        reward = None
        done = False
        
        # We must pick a number      
        draw = self.np_random.binomial(1, 1 - self.alpha, 1)
        
        matchsum = action + draw
        
        # Environment of when environment wins.
        envwins = ((matchsum % 2) == self.chosen) 
        
        reward = int(not envwins)
        
        self.chosen = self._choose()
        obs = np.append(self.chosen, draw)
        
        return obs, reward, done, {}

    def _choose(self):    
        chosen = self.np_random.binomial(1, 1 - self.beta, 1)
        return (chosen)
    
    def reset(self):
        self.chosen = self._choose()
        return np.append(self.chosen, 0)
    
    def render(self, mode=None):
        pass
    
    
    def close(self):
        pass


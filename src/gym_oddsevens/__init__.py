from gym.envs.registration import register
 
register(
    id='OddsEvens-v0',
    entry_point='gym_oddsevens.envs:OddsEvensBiasedEnv', 
    max_episode_steps=100,
    reward_threshold=80
)

register(
    id='OddsEvensAdversarial-v0',
    entry_point='gym_oddsevens.envs:OddsEvensAdversarialHardEnv', 
    max_episode_steps=100
)

register(
    id='OddsEvensAdversarial-v1',
    entry_point='gym_oddsevens.envs:OddsEvensAdversarialSoftEnv', 
    max_episode_steps=100
)


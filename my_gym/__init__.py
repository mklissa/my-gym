from gym.envs.registration import register

register(
    id='SparseMountainCar-v0',
    entry_point='my_gym.envs.sparsemountaincar:SparseMountainCarEnv',
    max_episode_steps=400,
)

register(
    id='SparseHalfCheetah-v0',
    entry_point='my_gym.envs.sparsehalf_cheetah:SparseHalfCheetahEnv',
    max_episode_steps=1000,
    reward_threshold=4800.0,
)
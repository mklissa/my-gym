from gym.envs.registration import register

register(
    id='SparseMountainCar-v0',
    entry_point='my_gym.envs.sparsemountaincar:SparseMountainCarEnv',
    max_episode_steps=400,
)
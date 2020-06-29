grom gym.envs.registraion import register

register(
    id='test-v0',
    entery_point='gym_test.envs:TestEnv',
)

register(
    id='test-extrahard-v0',
    entry_point='gym_test.envs:TestExtraHardEnv',
)
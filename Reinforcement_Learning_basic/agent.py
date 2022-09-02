import random
from env import SampleEnvironment


random.choice([0,1])

class Agent:
    def __init__(self):
        self.total_reward = 0.0

    def step(self, env: SampleEnvironment):
        current_obs = env.get_observation()
        print("Observation {}".format(current_obs))
        actions = env.get_actions()
        print(actions)
        reward = env.action(random.choice(actions))
        self.total_reward += reward
        print("Total Reward {}".format(self.total_reward))
from env import SampleEnvironment
from agent import Agent



if __name__ == "__main__":
    env = SampleEnvironment()
    agent = Agent()
    i=0

    while not env.is_done():
        i=i+1
        print("Steps {}".format(i))
        agent.step(env)

    print("Total reward got: %.4f" % agent.total_reward)
# Experiments with minerl

import minerl
import gym

import time

def exp():

    env = gym.make('MineRLNavigateDense-v0')
    # env.make_interactive(port= 5555, realtime=True)
    obs = env.reset()
    done = False
    net_reward = 0

    while not done:

        action = env.action_space.noop()

        action['camera'] = [0, 0.03 * obs["compass"]["angle"]]
        action['back'] = 0
        action['forward'] = 1
        action['jump'] = 1
        action['attack'] = 1

        obs, reward, done, info = env.step(
            action)

        net_reward += reward
        print("Total reward: ", net_reward)

        # Used to display what the agent is observing
        env.render()
        # # Used to slow down the rendering
        time.sleep(0.1)

    pass





if __name__ == "__main__":

    exp()

    pass
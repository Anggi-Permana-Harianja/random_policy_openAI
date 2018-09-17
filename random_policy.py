'''
- first reinforcement learning code
- using random search policy
- env: CartPole-V0
'''

import argparse
import sys

import gym
from gym import wrappers, logger

#create class RandomAgent
class RandomAgent(object):
	def __init__(self, action_space):
		self.action_space = action_space

	#action method
	def act(self, observation, reward, done):
		return self.action_space.sample()


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description = None)
	parser.add_argument('env_id', nargs = '?', default = 'SpaceInvaders-v0', help = 'select the environment to run')
	args = parser.parse_args()

	#set logger, you could set .INFO, .DEBUG, .WARN according to amount of output
	logger.set_level(logger.INFO)

	#create environment
	env = gym.make(args.env_id)


	outdir = '../random_agent_result/'
	env = wrappers.Monitor(env, directory = outdir, force = True)
	env.seed(0)

	#create agent
	agent = RandomAgent(env.action_space)

	episode_count = 100
	reward = 0
	done = False

	for i in range(episode_count):
		#initial observation
		ob = env.reset()
		while True:
			#set action
			env.render()
			action = agent.act(ob, reward, done)
			#get the respond from environment
			ob, reward, done, _ = env.step(action)

			if done:
				print('it is fucking done')
				break

	try:
		del env
	except ImportError:
		pass

	env.env.close()
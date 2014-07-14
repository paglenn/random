import random
import numpy as np
def random_step(d,endpoint=0):

	positions = range(d)
	zero_position = random.choice(positions)
	step = np.random.choice([-1,1],d)

	step[zero_position] = 0

	return step





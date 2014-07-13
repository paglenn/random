import random
import numpy as np
def random_step(d):

	positions = range(d)
	zero_position = random.choice(positions)
	step = np.random.choice([-1,1],d)
	step[zero_position] = 0

	return step

for i in range(8):
	print random_step(3)




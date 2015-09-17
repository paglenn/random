import random, math

L = 16
N = L * L
nbr = {i : ((i // L) * L + (i + 1) % L, (i + L) % N,
            (i // L) * L + (i - 1) % L, (i - L) % N) \
                                    for i in range(N)}
nsteps = 100000
TRANGE = [0.01,0.5,1.0,2.0,3.0,4.0,5.0]
T = 2.0
beta = 1.0 / T
S = [random.choice([1, -1]) for k in range(N)]
M = [sum(S) ]
for step in range(nsteps):
    k = random.randint(0, N - 1)
    delta_E = 2.0 * S[k] * sum(S[nn] for nn in nbr[k])
    if random.uniform(0.0, 1.0) < math.exp(-beta * delta_E):
        S[k] *= -1

    M.append(sum(S))


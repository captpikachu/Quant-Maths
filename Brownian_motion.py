import numpy as np

def simulate_bm(n, num_paths, T):
    dt = T / n
    steps = np.random.choice([-1, 1], size=(num_paths, n)) * np.sqrt(dt)
    W = np.cumsum(steps, axis=1)
    W = np.hstack([np.zeros((num_paths, 1)), W])
    t = np.linspace(0, T, n + 1)
    return t, W

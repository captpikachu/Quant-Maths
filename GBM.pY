import numpy as np

def simulate_gbm(S0, mu, sigma, T, N, M):
    dt = T/N
    Z = np.random.randn(M, N)

    returns = ((mu - 0.5 * sigma**2)*dt + sigma*np.sqrt(dt)*Z)

    price_paths = S0 *np.exp(np.cumsum(returns, axis=1))
    price_paths = np.hstack([S0 * np.ones((M, 1)), price_paths])

    t = np.linspace(0, T,N + 1)
    ST = price_paths[:, -1]
    return t, price_paths, ST
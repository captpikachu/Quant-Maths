import numpy as np

def terminal_stock_prices(S0,r,sigma,T,M):
    Z = np.random.randn(M)
    ST = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)
    return ST 

def european_call_mc(S0, K, r, sigma, T, M):
    ST = terminal_stock_prices(S0, r, sigma, T, M)
    payoffs = np.maximum(ST - K, 0)
    discounted_payoffs = np.exp(-r * T) * payoffs
    price = np.mean(discounted_payoffs)
    std_err = np.std(discounted_payoffs, ddof=1) / np.sqrt(M)
    return price, std_err, ST

def european_put_mc(S0, K, r, sigma, T, M):
    ST = terminal_stock_prices(S0, r, sigma, T, M)
    payoffs = np.maximum(K - ST, 0)
    discounted_payoffs = np.exp(-r * T) * payoffs
    price = np.mean(discounted_payoffs)
    std_err = np.std(discounted_payoffs, ddof=1) / np.sqrt(M)
    return price, std_err, ST

def european_option_mc(S0, K, r, sigma, T, M, option_type="call"):
    if option_type == "call":
        return european_call_mc(S0, K, r, sigma, T, M)
    elif option_type == "put":
        return european_put_mc(S0, K, r, sigma, T, M)
    else:
        raise ValueError("option_type must be 'call' or 'put'")

def mc_convergence(S0, K, r, sigma, T, path_counts, option_type="call"):
    counts = np.asarray(path_counts, dtype=int)
    prices = np.empty(len(counts), dtype=float)
    std_errors = np.empty(len(counts), dtype=float)
    for i, M in enumerate(counts):
        price, std_err, _ = european_option_mc(S0, K, r, sigma, T, int(M), option_type)
        prices[i] = price
        std_errors[i] = std_err
    return counts, prices, std_errors
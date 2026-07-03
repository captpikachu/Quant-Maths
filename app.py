import streamlit as st
import matplotlib.pyplot as plt
from Brownian_motion import simulate_bm
from GBM import simulate_gbm
from MonteCarloPricing import european_option_mc, mc_convergence
st.set_page_config(page_title="QuantMath", layout="wide")
st.title("QuantMath")

tab1, tab2,tab3 = st.tabs(["Brownian Motion", "GBM","Monte Carlo Pricing"])

with tab1:
    n = st.slider("BM steps", 100, 50000, 10000, step=100)
    paths = st.slider("BM paths", 1, 10, 3)
    T = st.slider("BM time", 1.0, 10.0, 1.0, step=0.5)

    t, W = simulate_bm(n, paths, T)
    fig, ax = plt.subplots()
    ax.plot(t, W.T)
    ax.set_xlabel("Time")
    ax.set_ylabel("W(t)")
    st.pyplot(fig)

with tab2:
    S0 = st.slider("S0", 1.0, 1000.0, 100.0)
    mu = st.slider("mu", -0.5, 0.5, 0.08, step=0.01)
    sigma = st.slider("sigma", 0.01, 2.0, 0.2, step=0.01)
    T = st.slider("T", 0.1, 5.0, 1.0, step=0.1)
    N = st.slider("N", 10, 2000, 250, step=10)
    M = st.slider("M", 1, 1000, 100)

    t, price_paths, ST = simulate_gbm(S0, mu, sigma, T, N, M)

    fig, ax = plt.subplots()
    ax.plot(t, price_paths[:min(M, 30)].T, linewidth=0.8)
    ax.set_xlabel("Time")
    ax.set_ylabel("Price")
    st.pyplot(fig)

with tab3:
    st.header("European Option Pricing")
 
    option_type = st.radio(
        "Option type", ["call", "put"], horizontal=True, key="mc_type"
    )
 
    S0 = st.slider("Initial Stock Price", 1.0, 500.0, 100.0, key="mc_s0")
    K = st.slider("Strike Price", 1.0, 500.0, 110.0)
    r = st.slider("Risk-Free Rate", 0.0, 0.20, 0.05)
    sigma = st.slider("Volatility", 0.01, 1.0, 0.20, key="mc_sigma")
    T = st.slider("Maturity (Years)", 0.1, 5.0, 1.0, key="mc_T")
    M = st.slider("Monte Carlo Simulations", 100, 100000, 10000)
 
    # Prices
    mc_price, mc_std_err, ST = european_option_mc(S0, K, r, sigma, T, M, option_type)
 
    ci_lower = mc_price - 1.96 * mc_std_err
    ci_upper = mc_price + 1.96 * mc_std_err
 
    c1, c2, c3 = st.columns(3)
    c1.metric("Monte Carlo Price Estimate", f"{mc_price:.4f}")
    c2.metric("Standard Error (SE)", f"{mc_std_err:.4f}")
    c3.metric("95% Confidence Interval", f"[{ci_lower:.4f}, {ci_upper:.4f}]")
 
    # Terminal price distribution (your original chart, kept)
    fig, ax = plt.subplots()
    ax.hist(ST, bins=40, edgecolor="black")
    ax.axvline(K, color="red", linestyle="--", label="Strike Price")
    ax.set_xlabel(r"$S_T$")
    ax.set_ylabel("Frequency")
    ax.set_title("Distribution of Terminal Stock Prices")
    ax.legend()
    st.pyplot(fig)
 
    # Convergence experiment
    st.subheader("Monte Carlo Convergence & Confidence Bands")
    path_counts = [100, 500, 1000, 5000, 10000, 50000, 100000]
    counts, prices, std_errs = mc_convergence(S0, K, r, sigma, T, path_counts, option_type)
 
    fig3, ax3 = plt.subplots()
    ax3.plot(counts, prices, marker="o", color="blue", label="Monte Carlo Estimate")
    ax3.fill_between(counts, prices - 1.96 * std_errs, prices + 1.96 * std_errs, color="blue", alpha=0.15, label="95% Confidence Interval")
    ax3.set_xscale("log")
    ax3.set_xlabel("Number of simulations (log scale)")
    ax3.set_ylabel("Option price")
    ax3.set_title("Monte Carlo price vs number of simulations")
    ax3.legend()
    st.pyplot(fig3)
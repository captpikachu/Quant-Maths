import streamlit as st
import matplotlib.pyplot as plt
from Brownian_motion import simulate_bm
from GBM import simulate_gbm

st.set_page_config(page_title="QuantMath", layout="wide")
st.title("QuantMath")

tab1, tab2 = st.tabs(["Brownian Motion", "GBM"])

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
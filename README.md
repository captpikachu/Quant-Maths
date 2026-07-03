# QuantMath — Stochastic Processes & Option Pricing

An interactive Streamlit app that builds European option pricing from the
ground up: Brownian motion → Geometric Brownian Motion → Monte Carlo pricing
with statistical error analysis.

## Features

- **Brownian Motion** — simulate the Wiener process from a scaled random walk.
- **Geometric Brownian Motion** — simulate stock price paths and view the
  lognormal terminal-price distribution, with the Ito's-lemma derivation.
- **Monte Carlo Pricing** — price European **calls and puts** under the
  risk-neutral measure, calculate standard error & 95% confidence intervals, and visualise convergence with statistical error bands.

## Math at a glance

**GBM:** $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t \Rightarrow
S_t = S_0 e^{(\mu - \frac12\sigma^2)t + \sigma W_t}$

**Risk-neutral price:** $e^{-rT}\,\mathbb{E}^{\mathbb{Q}}[\text{payoff}(S_T)]$

**Standard Error (SE):** $SE = e^{-rT} \frac{s}{\sqrt{M}}$ (where $s$ is the sample standard deviation of the discounted payoffs, and $M$ is the number of simulations)

**95% Confidence Interval:** $[\hat{C} - 1.96 \cdot SE, \; \hat{C} + 1.96 \cdot SE]$

## Project structure

```
quantmath/
├── app.py                  # Streamlit UI (3 tabs)
├── Brownian_motion.py      # simulate_bm
├── GBM.py                  # simulate_gbm
├── MonteCarloPricing.py    # MC call/put + convergence & standard errors
├── requirements.txt
└── README.md
```

## Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

Opens at `http://localhost:8501`.

## Example (S0 = K = 100, r = 5%, σ = 20%, T = 1, Option = Call)

For $M = 100,000$ simulations, the price estimate might yield:
- **Price Estimate:** `≈ 10.45`
- **Standard Error:** `≈ 0.05`
- **95% Confidence Interval:** `[≈ 10.35, ≈ 10.55]`

## Possible next steps

- Variance reduction (antithetic variates) for faster convergence
- Path-dependent options (Asian, barrier) using the full GBM paths
- Black-Scholes closed-form benchmarking (comparing MC with the analytical formula)
- Option Greeks (sensitivities like delta, gamma, vega) using finite difference methods

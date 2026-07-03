# QuantMath —  Option Pricing

Extending the learning to build European option pricing from the
ground up: Brownian motion → Geometric Brownian Motion → Monte Carlo pricing.

## Features

- **Brownian Motion** — simulate the Wiener process from a scaled random walk.
- **Geometric Brownian Motion** — simulate stock price paths and view the
  lognormal price distribution.
- **Monte Carlo Pricing** — price European **calls and puts** under the
  risk-neutral measure, calculate standard error & 95% confidence intervals.

## Math at a glance

**GBM:** $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t \Rightarrow
S_t = S_0 e^{(\mu - \frac12\sigma^2)t + \sigma W_t}$

**Risk-neutral price:** $e^{-rT}\,\mathbb{E}^{\mathbb{Q}}[\text{payoff}(S_T)]$

**Standard Error (SE):** $SE = e^{-rT} \frac{s}{\sqrt{M}}$ (where $s$ is the sample standard deviation of the discounted payoffs, and $M$ is the number of simulations)

**95% Confidence Interval:** $[\hat{C} - 1.96 \cdot SE, \; \hat{C} + 1.96 \cdot SE]$

## Project structure

```
quantmath/
├── app.py                  # 
├── Brownian_motion.py      # simulate_bm
├── GBM.py                  # simulate_gbm
├── MonteCarloPricing.py    # MC call/put + convergence & standard errors
└── README.md
```

## Run

```bash
streamlit run app.py
```
#Requirements
- streamlit
- numpy
- matplotlib

## Possible next steps
- Black-Scholes closed-form benchmarking (comparing MC with the analytical formula)

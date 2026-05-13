import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
# -------------------------
# 1. Load Data
# -------------------------

# File paths
prices_path = Path("monthly_prices.csv")
returns_path = Path("monthly_returns.csv")

# Check files exist before loading
if not prices_path.exists():
    raise FileNotFoundError(f"{prices_path} not found")

if not returns_path.exists():
    raise FileNotFoundError(f"{returns_path} not found")

# Load CSVs
monthly_prices = pd.read_csv(prices_path, index_col=0, parse_dates=True)
monthly_returns = pd.read_csv(returns_path, index_col=0, parse_dates=True)


# -------------------------
# 10. Stock Risk & Return Metrics
# -------------------------

mean_returns = monthly_returns.mean()
std_dev = monthly_returns.std()
cv = std_dev / mean_returns

stock_summary = pd.DataFrame({
    "Mean Return": mean_returns,
    "Risk (Std Dev)": std_dev,
    "CV": cv
})

# -------------------------
# 11. Equal Weight Portfolio
# -------------------------

# Equal weights
num_stocks = len(monthly_returns.columns)
weights = np.array([1/num_stocks] * num_stocks)

print("\nPortfolio Weights:")
print(weights)

# -------------------------
# 12. Portfolio Return
# -------------------------

# Monthly portfolio returns
portfolio_returns = monthly_returns.dot(weights)

# Average portfolio return
portfolio_mean_return = portfolio_returns.mean()

print("\nPortfolio Mean Return:")
print(portfolio_mean_return)

# -------------------------
# 13. Portfolio Risk
# -------------------------

# Covariance matrix
cov_matrix = monthly_returns.cov()

# Portfolio variance
portfolio_variance = np.dot(weights.T,
                            np.dot(cov_matrix, weights))

# Portfolio standard deviation
portfolio_std = np.sqrt(portfolio_variance)

print("\nPortfolio Risk (Std Dev):")
print(portfolio_std)

# -------------------------
# 14. Portfolio Summary
# -------------------------

portfolio_cv = portfolio_std / portfolio_mean_return

portfolio_summary = pd.DataFrame({
    "Portfolio Return": [portfolio_mean_return],
    "Portfolio Risk": [portfolio_std],
    "CV": [portfolio_cv]
})

print("\n=== Portfolio Summary ===")
print(portfolio_summary)


# -------------------------
# 15. Compare Risk
# -------------------------

comparison = stock_summary.copy()

comparison.loc["Portfolio"] = [
    portfolio_mean_return,
    portfolio_std,
    portfolio_cv
]

print("\n=== Stock vs Portfolio Comparison ===")
print(comparison)

# -------------------------
# 16. Portfolio Returns Plot
# -------------------------

portfolio_returns.plot(
    figsize=(10,5),
    title="Equal-Weight Portfolio Returns"
)

plt.ylabel("Monthly Return")
plt.savefig("portfolio_returns.png")
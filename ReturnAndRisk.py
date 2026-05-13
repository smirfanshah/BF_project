# =========================
# PSX Fertilizer Sector Analysis
# =========================

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
# 6. Risk & Return Metrics
# -------------------------
mean_returns = monthly_returns.mean()
std_dev = monthly_returns.std()
cv = std_dev / mean_returns

summary = pd.DataFrame({
    "Mean Return": mean_returns,
    "Risk (Std Dev)": std_dev,
    "CV": cv
})

print("\n=== Summary ===")
print(summary)

print("\nHighest Return:")
print(mean_returns.idxmax())

print("\nMost Volatile:")
print(std_dev.idxmax())

print("\nBest Return Relative to Risk (Lowest CV):")
print(cv.idxmin())

# -------------------------
# 7. Save Outputs
# -------------------------
monthly_prices.to_csv("monthly_prices.csv")
monthly_returns.to_csv("monthly_returns.csv")
summary.to_csv("summary_stats.csv")

# -------------------------
# 8. Plot
# -------------------------
monthly_prices.plot(figsize=(10,6), title="Monthly Prices")
plt.savefig("monthly_prices.png")
plt.show()

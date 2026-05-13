import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import seaborn as sns

returns_path = Path("monthly_returns.csv")

# Check file exists before loading
if not returns_path.exists():
    raise FileNotFoundError(f"{returns_path} not found")

# Load CSV
monthly_returns = pd.read_csv(returns_path, index_col=0, parse_dates=True)

# -------------------------
# 9. Correlation Matrix
# -------------------------
correlation_matrix = monthly_returns.corr()

print("\n=== Correlation Matrix ===")
print(correlation_matrix)

# Save correlation matrix
correlation_matrix.to_csv("correlation_matrix.csv")

# -------------------------
# 10. Correlation Heatmap
# -------------------------
plt.figure(figsize=(8,6))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Stock Return Correlation Matrix")
plt.savefig("correlation_heatmap.png")
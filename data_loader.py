# =========================
# PSX Fertilizer Sector Data Loader
# =========================

import pandas as pd
import yfinance as yf

# -------------------------
# 1. Define Stocks
# -------------------------
tickers = {
    "FFC": "FFC.KA",
    "EFERT": "EFERT.KA",
    "FFBL": "FFBL.KA",
    "FATIMA": "FATIMA.KA",
    "AGL": "AGL.KA"
}

start_date = "2020-01-01"
end_date = "2026-05-01"

# -------------------------
# 2. Fetch Data
# -------------------------
price_data = pd.DataFrame()

for name, ticker in tickers.items():
    try:
        data = yf.download(ticker, start=start_date, end=end_date, auto_adjust=False)
        price_data[name] = data['Close']
        print(f"{name} loaded")
    except:
        print(f"{name} failed")

# -------------------------
# 3. Handle Missing Data
# -------------------------
price_data = price_data.dropna()

# -------------------------
# 4. Convert to Monthly
# -------------------------
monthly_prices = price_data.resample('ME').last()

# -------------------------
# 5. Calculate Returns
# -------------------------
monthly_returns = monthly_prices.pct_change().dropna()

# -------------------------
# 6. Save Data
# -------------------------
monthly_prices.to_csv("monthly_prices.csv")
monthly_returns.to_csv("monthly_returns.csv")

print("Data loaded and saved successfully.")
#!/usr/bin/env python
# coding: utf-8

# In[3]:


import yfinance as yf

def fetch_current_prices(tickers):
    data = yf.download(tickers, period="1d", group_by='ticker')
    current_prices = {ticker: data[ticker]['Close'].iloc[-1] for ticker in tickers}
    return current_prices

# Define your investment strategy (e.g., target percentages)
target_allocation = {'AAPL': 0.6, 'BND': 0.3, 'CASH': 0.1}

# Define your portfolio holdings (e.g., current shares)
portfolio_holdings = {'AAPL': 100, 'BND': 200, 'CASH': 1000}

# Fetch current market prices
current_prices = fetch_current_prices(target_allocation.keys())

# Calculate current portfolio value
portfolio_value = sum(current_prices[ticker] * portfolio_holdings[ticker] for ticker in target_allocation)

# Calculate current allocation percentages
current_allocation = {ticker: (current_prices[ticker] * portfolio_holdings[ticker]) / portfolio_value for ticker in target_allocation}

# Calculate required adjustments and execute trades
rebalance_threshold = 0.05
for ticker in target_allocation:
    if abs(current_allocation[ticker] - target_allocation[ticker]) > rebalance_threshold:
        # Calculate buy/sell quantities and place orders here
        pass

# Print portfolio summary
print("Current Allocation:", current_allocation)
print("Target Allocation:", target_allocation)


# In[4]:


import requests

def get_stock_price(symbol):
    response = requests.get(f"https://api.example.com/stock/{symbol}")
    data = response.json()
    return data['price']

# Initialize the portfolio with stocks and their current shares
portfolio = {'AAPL': 10, 'GOOGL': 5, 'AMZN': 8}

# Define the target weights for each stock
target_weights = {'AAPL': 0.4, 'GOOGL': 0.3, 'AMZN': 0.3}


# In[ ]:





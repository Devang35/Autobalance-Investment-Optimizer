#!/usr/bin/env python
# coding: utf-8

# In[1]:


def rebalance_portfolio(portfolio, target_weights):
    total_value = sum([get_stock_price(symbol) * shares for symbol, shares in portfolio.items()])
    new_portfolio = {}
    
    for symbol, shares in portfolio.items():
        target_value = total_value * target_weights[symbol]
        current_price = get_stock_price(symbol)
        new_shares = int(target_value / current_price)
        new_portfolio[symbol] = new_shares
    
    return new_portfolio


# In[ ]:


# Execution and Result Display
if __name__ == "__main__":
    print("Original Portfolio:", portfolio)
    new_portfolio = rebalance_portfolio(portfolio, target_weights)
    print("Rebalanced Portfolio:", new_portfolio)


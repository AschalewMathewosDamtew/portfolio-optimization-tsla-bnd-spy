from pyportfolioopt import EfficientFrontier
import numpy as np

def optimize_portfolio(returns):
    ef = EfficientFrontier(returns.mean(), returns.cov())
    weights = ef.max_sharpe()  # Maximize Sharpe ratio
    return weights

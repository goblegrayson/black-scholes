"""
model.py
A class to model the black scholes option pricing formula.
"""
from statistics import NormalDist
import numpy as np

class BlackScholes:
    def __init__(self):
        """Initialise the BlackScholes class"""
        # Time-value of money parameters:
        self.time = 0.0  # Days
        self.expiration_time = 0.0  # Days
        self.risk_free_rate = 0.0  # Annualized
        # Underlying parameters
        self.price_underlying = 0.0
        self.volatility = 0.0
        # Option parameters
        self.isCall = True  # True for call, False for put
        self.strike = 0.0

    @property
    def time_to_expiration(self):
        """Dynamic calculation of days until expiration"""
        return (self.expiration_time - self.time) / 365.25

    @property
    def option_price(self):
        """Dynamic calculation of option price"""
        # Input values
        sigma = self.volatility
        tte = self.time_to_expiration
        x = self.price_underlying
        c = self.strike
        r = self.risk_free_rate
        # Watch out for those 0DTEs
        if tte <= 0 and self.isCall:
            v = max(0.0, x - c)
            return v
        elif tte <= 0:
            v = max(0.0, c - x)
            return v
        # Price the option
        d1 = (np.log(x / c) + (r + ((sigma ** 2) / 2)) * tte) / (sigma * np.sqrt(tte))
        d2 = d1 - sigma * np.sqrt(tte)
        normal_dist = NormalDist(sigma=1)
        if self.isCall:
            w = x * normal_dist.cdf(d1) - c * np.exp(-r * tte) * normal_dist.cdf(d2)
        else:
            w = -x * normal_dist.cdf(-d1) + c * np.exp(-r * tte) * normal_dist.cdf(-d2)
        return np.round(w, 2)

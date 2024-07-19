"""
model.py
A class to model the black scholes option pricing formula.
"""
from statistics import NormalDist
import numpy as np

class BlackScholes:
    def __init__(self):
        # Time-value of money parameters:
        self.time = 0.0  # Days
        self.expiration_time = 0.0  # Days
        self.risk_free_rate = 0.0  # Annualized
        # Underlying parameters
        self.price_underlying = 0.0
        self.drift_rate = 0.0
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
        sigma = self.volatility
        mu = self.drift_rate
        tte = self.time_to_expiration
        s = self.price_underlying
        k = self.strike
        r = self.risk_free_rate
        d_plus = (np.log(s / k) + (r + ((sigma ** 2) / 2)) * tte) / (sigma * np.sqrt(tte))
        d_minus = d_plus - sigma * np.sqrt(tte)
        normal_dist = NormalDist(mu=mu, sigma=1)
        if self.isCall:
            c = normal_dist.cdf(d_plus) * s - normal_dist.cdf(d_minus) * k * np.exp(-r * tte)
            return round(c, 2)
        else:
            p = normal_dist.cdf(-d_minus) * k * np.exp(-r * tte) - normal_dist.cdf(-d_plus) * s
            return round(p, 2)


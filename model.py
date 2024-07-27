"""
model.py
A class to model the black scholes option pricing formula.
"""
from statistics import NormalDist
import numpy as np
import pandas as pd
from functools import cache


class BlackScholes:
    def __init__(self):
        """Initialise the BlackScholes class"""
        # Time-value of money parameters:
        self.time = np.float64(0.0)  # Days
        self.expiration_time = np.float64(0.0)  # Days
        self.risk_free_rate = np.float64(0.0)  # Annualized
        # Underlying parameters
        self.price_underlying = np.float64(0.0)
        self.volatility = np.float64(0.0)
        # Option parameters
        self.isCall = True  # True for call, False for put
        self.strike = np.float64(0.0)

    @property
    def time_to_expiration(self):
        """Dynamic calculation of days until expiration"""
        return (self.expiration_time - self.time) / 365.25

    @property
    def type_string(self):
        """Dynamic selection of type string"""
        if self.isCall:
            return 'Call'
        else:
            return 'Put'

    @property
    def option_price(self):
        """Dynamic calculation of option price"""
        # Input values
        vol = self.volatility
        tte = self.time_to_expiration
        x = self.price_underlying
        c = self.strike
        r = self.risk_free_rate
        is_call = self.isCall
        return self.calculate_option_price(vol, tte, x, c, r, is_call)

    @staticmethod
    @cache
    def calculate_option_price(vol, tte, x, c, r, is_call):
        """function to calculate option price"""
        # Watch out for those 0DTEs
        if tte <= 0 and is_call:
            v = max(0.0, x - c)
            return v
        elif tte <= 0:
            v = max(0.0, c - x)
            return v
        # Price the option
        d1 = (np.log(x / c) + (r + ((vol ** 2) / 2)) * tte) / (vol * np.sqrt(tte))
        d2 = d1 - vol * np.sqrt(tte)
        normal_dist = NormalDist(sigma=1)
        if is_call:
            w = x * normal_dist.cdf(d1) - c * np.exp(-r * tte) * normal_dist.cdf(d2)
        else:
            w = -x * normal_dist.cdf(-d1) + c * np.exp(-r * tte) * normal_dist.cdf(-d2)
        return np.round(w, 2)


    def calculate_price_surface(self, vol_range, number_of_strikes):
        """function to calculate a price surface"""
        # Make sure our strike granularity is appropriate
        strike_granularities = np.float64([1.0, 0.5, 0.25, 0.1])
        strike = np.float64(self.strike)
        strike_min_requested = strike - (number_of_strikes // 2) * strike_granularities
        strike_granularity = strike_granularities[np.argmax(strike_min_requested >= 0)]
        strike_min = strike - (number_of_strikes // 2) * strike_granularity
        strike_max = strike + (number_of_strikes // 2) * strike_granularity
        # Come up with our vectors for stike and vol
        vol = np.float64(self.volatility)
        vols = np.linspace(np.max([0, vol - vol_range]), vol + vol_range, number_of_strikes)
        strikes = np.linspace(strike_min, strike_max, number_of_strikes)
        price_surface = np.empty((len(vols), number_of_strikes))
        for i_strike, strike in enumerate(strikes):
            for i_vol, vol in enumerate(vols):
                price_surface[i_vol, i_strike] = self.calculate_option_price(
                    vol,
                    self.time_to_expiration,
                    self.price_underlying,
                    strike,
                    self.risk_free_rate,
                    self.isCall
                )
        # Convert to a pandas dataframe
        strike_labels = [f'${x:.2f}' for x in strikes]
        vol_labels = [f'{100*x:.2f}%' for x in vols]
        price_surface = pd.DataFrame(price_surface, columns=strike_labels, index=vol_labels)
        strikes, vols = np.meshgrid(strikes, vols)
        return price_surface, strikes, vols
"""
tests.py
Tests for black_scholes module.
"""
import pytest
import black_scholes


def test_init():
    model = black_scholes.BlackScholes()
    assert isinstance(model, black_scholes.BlackScholes)
    # Time-value of money parameters. Times in days and zero indexed
    assert model.time == 0
    assert model.expiration_time == 0
    assert model.risk_free_rate == 0.0
    # Underlying parameters
    assert model.price_underlying == 0.0
    assert model.drift_rate == 0.0
    assert model.volatility == 0.0
    # Option parameters
    assert model.isCall
    assert model.strike == 0.0


def test_time_to_expiration():
    model = black_scholes.BlackScholes()
    model.time = 0
    model.expiration_time = 30
    assert model.time_to_expiration == 30 / 365.25


def test_price_call():
    model = black_scholes.BlackScholes()
    # Time-value of money parameters. Times in days and zero indexed
    model.time = 0
    model.expiration_time = 3 * 365.25 / 12
    model.risk_free_rate = 0.01
    # Underlying parameters
    model.price_underlying = 100.0
    model.drift_rate = 0.0
    model.volatility = 0.5
    # Option parameters
    model.strike = 95.0
    model.isCall = True  # True for call, False for put
    # Hardcode values pulled from https://www.omnicalculator.com/finance/black-scholes
    assert round(model.option_price, 2) == 12.53
    model.isCall = False
    assert round(model.option_price, 2) == 7.29


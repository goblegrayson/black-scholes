"""
tests.py
Tests for black_scholes module.
"""
import pytest
import model


def test_init():
    bs = model.BlackScholes()
    assert isinstance(bs, model.BlackScholes)
    # Time-value of money parameters. Times in days and zero indexed
    assert bs.time == 0
    assert bs.expiration_time == 0
    assert bs.risk_free_rate == 0.0
    # Underlying parameters
    assert bs.price_underlying == 0.0
    assert bs.drift_rate == 0.0
    assert bs.volatility == 0.0
    # Option parameters
    assert bs.isCall
    assert bs.strike == 0.0


def test_time_to_expiration():
    bs = model.BlackScholes()
    bs.time = 0
    bs.expiration_time = 30
    assert bs.time_to_expiration == 30 / 365.25


def test_price_call():
    bs = model.BlackScholes()
    # Time-value of money parameters. Times in days and zero indexed
    bs.time = 0
    bs.expiration_time = 3 * 365.25 / 12
    bs.risk_free_rate = 0.01
    # Underlying parameters
    bs.price_underlying = 100.0
    bs.drift_rate = 0.0
    bs.volatility = 0.5
    # Option parameters
    bs.strike = 95.0
    bs.isCall = True  # True for call, False for put
    # Hardcode values pulled from https://www.omnicalculator.com/finance/black-scholes
    assert round(bs.option_price, 2) == 12.53
    bs.isCall = False
    assert round(bs.option_price, 2) == 7.29


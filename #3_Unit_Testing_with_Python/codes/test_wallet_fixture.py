# test_wallet_fixture.py

import pytest
from wallet import Wallet, NotEnoughCash

# wallet_0 returns an instance of Wallet with balance of 0
@pytest.fixture
def wallet_0():
    return Wallet()

# wallet_50 returns an instance of Wallet with balance of 50
@pytest.fixture
def wallet_50():
    return Wallet(50)

def test_default_initial_amount(wallet_0):
    assert wallet_0.balance == 0

def test_setting_initial_amount(wallet_50):
    assert wallet_50.balance == 50

def test_wallet_add(wallet_0):
    wallet_0.add(30)
    assert wallet_0.balance == 30

def test_wallet_spend(wallet_50):
    wallet_50.spend(30)
    assert wallet_50.balance == 20

def test_wallet_spend_cash_raises_exception_on_not_enough_cash(wallet_50):
    with pytest.raises(NotEnoughCash):
        wallet_50.spend(100)

# test_wallet.py

import pytest
from wallet import Wallet, NotEnoughCash


def test_default_initial_amount():
    wallet = Wallet()
    assert wallet.balance == 0

def test_setting_initial_amount():
    wallet = Wallet(50)
    assert wallet.balance == 50

def test_wallet_add():
    wallet = Wallet()
    wallet.add(30)
    assert wallet.balance == 30

def test_wallet_spend():
    wallet = Wallet(50)
    wallet.spend(30)
    assert wallet.balance == 20

def test_wallet_spend_cash_raises_exception_on_not_enough_cash():
    wallet = Wallet(50)
    with pytest.raises(NotEnoughCash):
        wallet.spend(100)


# test_wallet_fixture_parametrize.py

import pytest
from wallet import Wallet, NotEnoughCash

# wallet_50 returns an instance of Wallet with balance of 50
@pytest.fixture
def wallet_50():
    return Wallet(50)

@pytest.mark.parametrize("spent, expected", [
    (0, 50),
    (10, 40),
    (20, 30),
    (30, 20),  
    (40, 10),
    (50, 0),          
])
def test_transactions(wallet_50, spent, expected):
    wallet_50.spend(spent)
    assert wallet_50.balance == expected
    
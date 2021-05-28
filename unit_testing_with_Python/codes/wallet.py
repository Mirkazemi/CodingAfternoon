# wallet.py

class NotEnoughCash(Exception):
    pass

class Wallet(object):

    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def spend(self, amount):
        if self.balance < amount:
            raise NotEnoughCash(f'Not enough cash available to spend {amount}')
        self.balance -= amount

    def add(self, amount):
        self.balance += amount

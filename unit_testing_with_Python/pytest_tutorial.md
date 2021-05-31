# Unit testing in Python

What is unit testing?
Unit testing is a software development practice by which individual units of a code with associated data and usage procedures are tested to determine whether they are fit for use.

Why unit testing?
Code covered with tests is more reliable than the code without. Unit testing ensures that each unit of the code fulfils required functionalities individually. If a future change breaks something in the code, developers will be able to identify the root of the problem right away rather than coming through an unwieldy codebase to find the issue.

_pytest_ and _unittest_ are two popular unit testing frameworks for Python. The _unittest_ is a built-in Python package and provides a solid base on which to build your test suite, but it has an important shortcoming. In comparison to the pytest, for _unittest_ a significant amount of code is needed to write.

# Install pytest
To install _pytest_, run the following command in your command line:

```console$ pip install -U pytest```
or
```console$ pip3 install -U pytest```

You can check if _pytest_ is already installed:
```console$ pytest --versionpytest 6.2.4```

# Arrange-Act-Assert (AAA) model
Arrange-Act-Assert is a simple but powerful pattern to structure test cases. It directs an order of operations:
1. **Arrange:** Setting up inputs, targets and conditions for the test. Does the test requires, for example:   
  * any objects or special settings?   
  * to download or read a dataset or variables?   
  * to log into a web app?  
2. **Act:** Calling some function or method on the target behavior. Act steps should cover the main thing to be tested.
3. **Assert:** Assert that some end condition is true or in other words hee outcome of the act is as expected. Act steps should bring out some sort of outcomes or responses. Assert steps verify the goodness or badness of that response. For example, sometimes, assertions are checking numeric or string values. Assertions will ultimately determine if the test passes or fails.

# First example: Assert
Let's write small tests just to check if _pytest_ is working properly and get some intuition about how it works. We write one test that always passes and another always fails. Please consider that the below only contains **assert** steps.
```
# test_dummy.py

def test_always_true():
    assert True
    
def test_always_false():
    assert False
```
  
Now we may ask your Python to run the _pytest_:
```
$ python3 -m pytest

======================================== test session starts ========================================
platform darwin -- Python 3.8.0, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /path_to_the_working_directory/
plugins: anyio-2.2.0
collected 2 items                                                                                   
test_dummy.py .F                                                                              [100%]
============================================= FAILURES ==============================================
_________________________________________ test_always_false _________________________________________
    def test_always_false():>       assert FalseE       assert False
test_dummy.py:5: AssertionError
====================================== short test summary info ======================================
FAILED test_dummy.py::test_always_false - assert False
==================================== 1 failed, 1 passed in 0.11s ====================================
```

The results of the _pytest_ run are presented like above. The first block (test session starts) shows the system state like Python and pytest versions, root directory, and installed plugins in the first three lines. The other lines indicated the discovered tests. The next block lists the failed tests.
There are three signs of _._(dot with green color), _F_ (with red color) and _E_ (with red color) in the _pytest_ output that indicate passed test, failed test and raising an unexpected exception in a test.

# _pytest_ syntax
What exactly _pytest_ command do? In the root directory, _pytest_ looks for ```test_*.py``` 
and ```*_test.py``` files. In such files, _pytest_ looks for ```test``` prefixed test functions, like ```test_func1()```, and runs them.
The user can asks _pytest_ to specifically run test functions in a module and skip all other modules
```
$ python3 -m pytest test_module1.py
```
or to run specific test function in a test module
```
$ python3 -m pytest test_module1.py::test_funct1.py
```
where ```test_funct1.py``` is a test function in ```test_module1.py``` module.
For example, we ask _pytest_ to only run ```test_always_true()``` in ```test_dummy.py``` by
```
$ python3 -m pytest test_dummy.py::test_always_true
```
and the output is
```
======================================== test session starts ========================================
platform darwin -- Python 3.8.0, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /Users/mohammad.mirkazemi/Documents/Afternoon Coding/unit_testing
plugins: anyio-2.2.0
collected 1 item                                                                                    
test_dummy.py .                                                                               [100%]
========================================= 1 passed in 0.01s =========================================
```
that shows only ```test_always_true``` was run.

# Second example: Arrange-Act-Assert
Now let's write a more serious example of unit testing. Assuming that we wrote two functions for calculating the perimeter and area of a rectangle like the following. The _test_rectangle_area()_ test function is provided for _rectangle_area()_. Please write the other one test function, _test_rectangle_perimeter()_ for _rectangle_perimeter()_.
```
#test_rectangle_geo.py
def rectangle_area(x1, x2):
    return x1 * x2

def rectangle_perimeter(x1, x2):
    return 2 * (x1 + x2)

def test_rectangle_area():
    x1 = 3 # Arrange
    x2 = 4 # Arrange
    expected_area = 12 # Arrange
    calculated_area = rectangle_area(x1, x2) # Act
    assert expected_area == calculated_area # Assert

#Please implement the following test function for testing rectangle_perimeter() 
def test_rectangle_perimeter():
    # Arrange
    # Act    
    # Assert

```

Let's test run _pytest_ on ```test_rectangle_geo.py```:

```
$ python3 -m pytest test_rectangle_geo.py
```

# 3rd example: Unit testing for a class

Now we work on a more realistic example. Assume that we have a class of _Wallet_ with such properties:
- an instance of object is initiated with a given initial balance of money
- if no initial balance is provided the instance is generated with defaut balance of 0
- the balance of the a _Wallet_ instance is saved in ```balance``` attribute
- one can add cash to a _Wallet_ instance using ```add``` method
- one can add spend from a _Wallet_ instance using ```spend``` method
- if one wants to spend more than ```balance``` of the _Wallet_ instance, an NotEnoughCash exception should be raised.
The _Wallet_ class with such properties can be implemented as below.

```
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

```

We write a set of unit tests to test desired properties of the class _Wallet_. Please complete the incomplete test functions:

```
# test_wallet.py

import pytest
from wallet import Wallet, NotEnoughCash


def test_default_initial_amount():
    wallet = Wallet()
    assert wallet.balance == 0

# implement test_setting_initial_amount() test function to set 50 as initial amount
def test_setting_initial_amount():
    ....

def test_wallet_add():
    wallet = Wallet()
    wallet.add(30)
    assert wallet.balance == 30
    
# implement test_wallet_spend() test function to initiate a Wallet object with 50 and spend 30 and then test the expected balance 20
def test_wallet_spend():
    ....

def test_wallet_spend_cash_raises_exception_on_not_enough_cash():
    wallet = Wallet(50)
    with pytest.raises(NotEnoughCash):
        wallet.spend(100)

```
After completing the above test module you may run it by
```
python3 -m pytest test_wallet.py 
```
# 4rd example: refactoring with _fixture_

Perhaps you have noted some repetition of coding for initializing objects in each test. We initialize two times the same _Wallet_ instance with an initial amount of zero and three times with initial amounts of 50. In big projects, sometimes each **arrange** step needs a large amount of coding since it may need reading a database, extracting a subset, some calculation, etc. The _pytest_ have a solution to reduce the amount of boilerplate code in such cases. Fixtures help us set up some helper code. They should run in order to **arrange** the tests before any tests are executed.

Lets see how fixtures work in practice. Since we had two groups of instance creation with zero and 50 initial amounts, we wrote two fixtures to make objects with the desired initial amount. Then each test function takes a suitable fixture function.

```
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

# Implement test_setting_initial_amount test function in order to test the balance of Wallet instance with initial amount of 50 
def test_setting_initial_amount
    ...

def test_wallet_add(wallet_0):
    wallet_0.add(30)
    assert wallet_0.balance == 30

# Implement test_setting_initial_amount test function in order to test the balance of Wallet instance initiated with 50 after spending 30
def test_wallet_spend
    ...

def test_wallet_spend_cash_raises_exception_on_not_enough_cash(wallet_50):
    with pytest.raises(NotEnoughCash):
        wallet_50.spend(100)
        
```

# Summary
Unit testing is one of the software testing practices by which the smallest components of a software are tested individually. It also helps you to find the probable bugs which are created by future changes in the code. The AAA (Arrange-Act-Assert) pattern is a standard for software testing:

- Arrange: create target objects (like test data)
- Act: apply the tested method
-  Assert: check whether the expectations were met

_pytest_ is a powerful and easy-to-use tool for unit testing. It enables a programmer to test the outcome of a method or function with few lines of code. It also provides _fixture_ functions to prevent writing boilerplate codes to generate testing data. 

# test_Account.py
import pytest
from src.Account import Account

def test_deposit():
    # set up
    account = Account(1234, "John Doe", 100.0, "Checking")

    # func call
    account.deposit(50.0)

    # actual output
    actual_output = account.curr_balance

    # expected output
    expected_output = 150.0

    # check deposit amount
    assert actual_output == expected_output

    # check ValueError
    with pytest.raises(ValueError):
        account.deposit(-100.0)

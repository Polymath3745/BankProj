# test_Account.py
import pytest
from src.Account import Account
"""
Test the deposit method of the Account class
"""
def test_deposit():
    # Arrange: Set up the initial account state
    account = Account(1234, "John Doe", 100.0, "Checking")

    # Act: Perform the deposit operation
    account.deposit(50.0)

    # Assert: Check the results
    actual_output = account.curr_balance
    expected_output = 150.0

    assert actual_output == expected_output

    # Check the ValueError for negative deposit
    with pytest.raises(ValueError):
        account.deposit(-100.0)

"""
test_Account.py
"""

# test packages
import pytest
from unittest.mock import patch
import io

# UUT
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

"""
Test the withdraw method of the Account class
"""
def test_withdraw():
    # Arrange: Set up the initial account state
    account = Account(1234, "John Doe", 100.0, "Checking")

    # Act: Perform the withdraw operation
    account.withdraw(50.0)

    # Assert: Check results of withdraw operation
    actual_output = account.curr_balance
    expected_output = 50.0
    assert actual_output == expected_output

    # Act: Perform withdraw operation (zero balance case) 
    #      capture print output
    with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
        account.withdraw(50.0)
        output = mock_stdout.getvalue()

    # Assert: Check results of the withdraw operation
    #         check string output
    actual_output = account.curr_balance
    expected_output = 0.0
    assert actual_output == expected_output
    assert "Your account has zero dollars in it!" in output

    # Act: Perform withdraw opertion (negative balance case)
    #      capture print output
    with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
        account.withdraw(50.0)
        output = mock_stdout.getvalue()

    # Assert: Check results of the withdraw opertaion
    actual_output = account.curr_balance
    expected_output = -50.0
    assert actual_output == expected_output
    assert "Your account has a negative balance!" in output

    # Check ValueError for negative withdrawl
    with pytest.raises(ValueError) as excinfo:
        account.withdraw(-100.0)
    
    # Check the exception message
    assert str(excinfo.value) == "Invalid withdrawal value"
class Account:
    """
    Creates an Account object

    This function constructs a new account object

    Args:
        accnt_num (float): the associated account number
        accnt_name (str): the associated account name
        curr_balance (float): the current monetary balance of the account
        accnt_type (str): the type of account, i.e., checkings, savings
    """
    def __init__(self, accnt_num: float, accnt_name: str, curr_balance: float, accnt_type: str):
        self.accnt_num = accnt_num
        self.accnt_name = accnt_name
        self.curr_balance = curr_balance
        self.accnt_type = accnt_type

    """
    Get Account number

    Args:
        self (Account): account object

    Return:
        float: the associated account number
    """
    @property
    def accnt_num(self):
        return self._accnt_num
    
    """
    Set Account number

    Args:
        self (Account): account object
        val (float): account number
    """
    @accnt_num.setter
    def accnt_num(self, val):
        if val >= 0:
            self._accnt_num = val
        else:
            raise ValueError("Account number must not be negative")
    
    """
    Get Account name

    Args:
        self (Account): account object

    Return:
        str: the associated account name
    """
    @property
    def accnt_name(self):
        return self._accnt_name
    
    """
    Set Account name

    Args:
        self (Account): account object
        name (str): account name
    """
    @accnt_name.setter
    def accnt_name(self, name):
        if name != "":
            self._accnt_name = name
        else:
            raise ValueError("Account name must not be empty")

    """
    Get Account balance

    Args:
        self (Account): account object

    Return:
        float: the associated account balance
    """
    @property
    def curr_balance(self):
        return self._curr_balance
    
    """
    Set Account balance

    Args:
        self (Account): account object
        val (float): account balance
    """
    @curr_balance.setter
    def curr_balance(self, val):
        self._curr_balance = val

    """
    Get Account type

    Args:
        self (Account): account object

    Return:
        str: the associated account type
    """
    @property
    def accnt_type(self):
        return self._accnt_type
    
    """
    Set Account type

    Args:
        self (Account): account object
        type (str): account type
    """
    @accnt_type.setter
    def accnt_type(self, type):
        if type != "":
            self._accnt_type = type
        else:
            raise ValueError("Account type must not be empty")

    """
    Deposits money into account

    Args:
        self (Account): account object
        val (float): deposit amount
    """
    def deposit(self, val):
        if val >= 0:
            self.curr_balance += val
        else:
            raise ValueError("Invalid deposit value")

    """
    Withdraw money from account

    Args:
        self (Account): account object
        val (float): withdrawal amount
    """
    def withdraw(self, val):
        if val > 0:
            self.curr_balance -= val
            if self.curr_balance == 0:
                print("Your account has zero dollars in it!")
            elif self.curr_balance < 0:
                print("Your account has a negative balance!")
        else:
            raise ValueError("Invalid withdrawal value")

    """
    Check balance of account

    Args:
        self (Account): account object

    Return:
        curr_balance (float): account _curr_balance
    """
    def check_balance(self):
        return self.curr_balance
    
    """
    Displays account info to the command line

    Args:
        self (Account): account object
    """
    def display_info(self):
        print(f'Account number: {self.accnt_num}\n Account name: {self.accnt_name}\n Balance: {self.curr_balance}\n Type: {self.accnt_type}')
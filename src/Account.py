class Account:
    """
    Creates an Account obj

    This function constructs a new account obj

    Args:
        accntNum(float): the associated account number
        accntName(str): the associated account name
        currBalance(float): the current monetary balance of the account
        accntType: the type of account i.e. checkings, savings
    """
    def __init__(self, accntNum: float, accntName: str, currBalance: float, accntType: str):
        self.accntNum = accntNum
        self.accntName = accntName
        self.currBalance = currBalance
        self.accntType = accntType

    """
    Get Account number

    Args:
        self(Account): account obj

    Return:
        float: the associated account number
    """
    @property
    def accntNum(self):
        return self._accntNum
    
    """
    Set Account number

    Args:
        self(Account): account obj
        val(float): account number
    """
    @accntNum.setter
    def accntNum(self, val):
        if(val >= 0):
            self._accntNum = val
        else:
            raise ValueError("Account number must not be negative")
    
    """
    Get Account name

    Args:
        self(Account): account obj

    Return:
        str: the associated account name
    """
    @property
    def accntName(self):
        return self._accntName
    
    """
    Set Account name

    Args:
        self(Account): account obj
        name(str): account name
    """
    @accntName.setter
    def accntName(self, name):
        if(name != ""):
            self._accntName = name
        else:
            raise ValueError("Account name must not be empty")

    """
    Get Account balance

    Args:
        self(Account): account obj

    Return:
        float: the associated account balance
    """
    @property
    def currBalance(self):
        return self._currBalance
    
    """
    Set Account balance

    Args:
        self(Account): account obj
        val(float): account balance
    """
    @currBalance.setter
    def currBalance(self, val):
        self._currBalance = val

    """
    Get Account type

    Args:
        self(Account): account obj

    Return:
        str: the associated account type
    """
    @property
    def accntType(self):
        return self._accntType
    
    """
    Set Account type

    Args:
        self(Account): account obj
        type(str): account type
    """
    @accntType.setter
    def accntType(self, type):
        if(type != ""):
            self._accntType = type
        else:
            raise ValueError("Account type must not be empty")

    """
    Deposits money into account

    Args:
        self(Account): account obj
        val(float): deposit amount
    """
    def deposit(self, val):
        if(val >= 0):
            self.currBalance += val
        else:
            raise ValueError("invalid deposit value")

    """
    Withdraw money from account

    Args:
        self(Account): account obj
        val(float): withdrawl amount
    """
    def withdraw(self, val):
        if(val >= 0):
            self.currBalance -= val
        if(self.currBalance == 0):
            print("Your account has zero dollars in it!")
        elif(self.currBalance < 0):
            print("Your account has a negative balance!")
        else:
            raise ValueError("invalid withdrawl value")

    """
    Check balance of account

    Args:
        self(Account): account obj

    Return:
        currBalance(float): account _currBalance
    """
    def checkBalance(self):
        return self.currBalance
    
    """
    Displays account info to the command line

    Args:
        self(Account): account obj
    """
    def displayInfo(self):
        print(f'Account number: {self.accntNum}\n Account name: {self.accntName}\n Balance: {self.currBalance}\n Type: {self.accntType}')
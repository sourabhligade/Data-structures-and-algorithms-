#R-2.5 Use the techniques of Section 1.7 to revise the charge and make payment methods of the
#CreditCard class to ensure that the caller sends a number as a parameter.



class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer, bank, acnt, limit):
        """Create a new credit card instance.
        The initial balance is zero.

        customer -- the name of the customer (e.g., John Bowman)
        bank -- the name of the bank (e.g., California Savings)
        acnt -- the account identifier (e.g., 5391 0375 9387 5309)
        limit -- credit limit (measured in dollars)
        """

        self.customer = customer
        self.bank = bank
        self.account = acnt
        self.limit = limit
        self.balance = 0

    def get_customer(self):
        """Return the name of the customer."""
        return self.customer

    def get_bank(self):
        """Return the bank's name."""
        return self.bank

    def get_account(self):
        """Return the card identifying number (typically stored as a string)."""
        return self.account

    def get_limit(self):
        """Return the current credit limit."""
        return self.limit

    def get_balance(self):
        """Return the current balance."""
        return self.balance

    def charge(self, price):
        if not isinstance(price(int,float)):
            raise TypeError('enter a number')
        
        if price + self.balance > self.limit:
            return False
        else:
            self.balance += price
            return True

    def make_payment(self, amount):
        if not isinstance(amount(int,float)):
            raise TypeError('enter a number')
        
        """Process customer payment that reduces the balance."""
        self.balance -= amount

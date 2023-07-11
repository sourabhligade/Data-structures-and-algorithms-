#The PredatoryCreditCard class of Section 2.4.1 provides a process month method that models the completion of a monthly cycle. Modify the
#class so that once a customer has made ten calls to charge in the current month, each additional call to that function results in an additional $1 surcharge.




class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees."""

    def __init__(self, customer, bank, acnt, limit, apr):
        """Create a new predatory credit card instance."""
        super().__init__(customer, bank, acnt, limit)  # call super constructor
        self.apr = apr
        self.charge_count = 0

    def charge(self, price):
        """Charge the given price to the card, assuming sufficient credit limit.
        Return True if the charge was processed.
        Return False and assess a $5 fee if the charge is denied.
        Apply a $1 surcharge for each additional charge after ten in a month.
        """
        success = super().charge(price)
        if not success:
            self.balance += 5
        else:
            self.charge_count += 1
            if self.charge_count > 10:
                self.balance += 1
        return success

    def process_month(self):
        """Assess monthly interest on the outstanding balance."""
        if self.balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self.apr, 1 / 12)
            self.balance *= monthly_factor
        self.charge_count = 0

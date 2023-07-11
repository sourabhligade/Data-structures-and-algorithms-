#Modify the PredatoryCreditCard class from Section 2.4.1 so that a cus- tomer is
#assigned a minimum monthly payment, as a percentage of the balance, and so that a 
#late fee is assessed if the customer does not subse- quently pay that minimum amount before the next monthly cycle.



class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees."""

    def __init__(self, customer, bank, acnt, limit, apr, min_payment_percentage, late_fee):
        """Create a new predatory credit card instance."""
        super().__init__(customer, bank, acnt, limit)  # call super constructor
        self.apr = apr
        self.min_payment_percentage = min_payment_percentage
        self.late_fee = late_fee
        self.minimum_payment_made = False

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
            self.minimum_payment_made = False
        return success

    def process_month(self):
        """Assess monthly interest on the outstanding balance and check for minimum payment."""
        if not self.minimum_payment_made:
            self.balance += self.late_fee

        if self.balance > 0:
            # Calculate the minimum payment
            min_payment = self.min_payment_percentage / 100 * self.balance

            if not self.minimum_payment_made:
                self.balance += min_payment  # Pay the minimum amount if not already paid

            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self.apr, 1 / 12)
            self.balance *= monthly_factor

        self.minimum_payment_made = True

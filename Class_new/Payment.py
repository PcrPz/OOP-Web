from Booking import *
from CreditCard import *
from System import *

class Payment:
    def __init__(self,amount, payment_status, transaction_id,credit_info):
        self._payment_status = payment_status 
        self._transaction_id = transaction_id 
        self._amount = amount
        self._credit_info = credit_info


    # def make_payment(self,balance,current_user = sym.get_current_user):
    #     if self.payment_status == False:
    #         if current_user.booking.get_price > balance:
    #             return "Payment insufficient"
    #         else:
    #             balance -= self.amount
    #             self.payment_status == True
    #             return "Payment sucsessful"
    
            
from datetime import datetime
import datetime
from abc import ABC , abstractmethod
from Booking import *
from CreditCard import *
import random
from Contact import Renter

class Payment:
    def __init__(self,amount, payment_status, transaction_id,credit_info):
        self.payment_status = payment_status 
        self.transaction_id = transaction_id 
        self.amount = amount 
        self.credit_info = credit_info
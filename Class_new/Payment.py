from datetime import datetime
from test_booked import Booking , CarRentalSystem
import random
import datetime
from abc import ABC , abstractmethod

class Payment:
    def __init__(self, amount, payment_method, payment_time):
        self.__amount = amount
        self.__payment_method = payment_method
        self.__payment_time = payment_time
        self.__transaction_id = None
        self.__payment_method_object = None
        
    def process_payment(self):
        self.__payment_method_object = self.__payment_method
        self.__payment_method_object.process_payment(self.__amount)

class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class BankTransfer(PaymentMethod):
    bankaccounts = []
    def __init__(self, bank_name, bank_account_number,balance):
        self.__bank_name = bank_name
        self.__bank_account_number = bank_account_number
        self.__balance = balance
        self.__transaction_id = None

    def get_bank_account_number(self):
        return self.__bank_account_number
    
    def get_bank_name(self):
        return self.__bank_name
    
    def add_account(self,account):
        self.bankaccounts.append(account)

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        self.__balance = amount

    def get_transaction_id(self):
        return self.__transaction_id
    
    def set_transaction_id(self, transaction_id):
        self.__transaction_id = transaction_id

    # Process bank transfer payment
    def process_payment(self, amount):
        # Validate bank account number  
        if self.__bank_account_number not in [account.get_bank_account_number() for account in self.bankaccounts]:
            return "Invalid bank account"
        if amount > self.get_balance():
            return "Insufficient balance"
        # Check available balance
        # Generate transaction ID
        else:
            self.set_balance(self.get_balance() - amount)
            self.set_transaction_id(random.randint(100000000,999999999))
            print(f"Payment successful")
            print(f"Transaction ID: {self.get_transaction_id()}")


class MobilePayment(PaymentMethod):
    def __init__(self, mobile_number):
        self.mobile_number = mobile_number
    
    def process_payment(self):
        # Process mobile payment
        # Validate mobile number
        # Check available balance
        # Generate transaction ID
        self.__transaction_id = random.randint(100000000,999999999)
        return f"Transaction_id: {self.transaction_id}"

class CreditCardPayment(PaymentMethod):
    def __init__(self, card_number, card_expiry_date, card_cvv):
        self.card_number = card_number
        self.card_expiry_date = card_expiry_date
        self.card_cvv = card_cvv
    
    def process_payment(self):
        # Process credit card payment
        # Validate card number, expiry date, and CVV
        # Check available balance
        # Generate transaction ID
        self.__transaction_id = random.randint(100000000,999999999)
        return f"Transaction_id: {self.transaction_id}"
    
system = CarRentalSystem()
bank1 = BankTransfer("Kasikorn", "0431747227", 1500)
bank1.add_account(bank1)
print(bank1.process_payment(Booking.get_rental_price()))



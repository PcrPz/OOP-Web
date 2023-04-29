from CreditInfo import *
import random
import string
class Payment: 
    def __init__(self,amount,card_info:CreditInfo): 
        self.__transaction_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        self.__amount = amount 
        self.__card_info = card_info
        
    def get_card_info(self):
        return self.__card_info
    
    def make_payment(self):
        if( not self.check_valid_card(self.__card_info.get_card_number())): 
            return "Invalid card" 
        status = self.perform_payment() 
        if status == True: 
            return "Payment success" 
        else : 
            return "Payment fail"

    def check_valid_card(self, card) -> bool: 
        if(len(card) == 16 and card.isdigit()): 
            return True 
        return False 
    
    def perform_payment(self) -> bool:
        return True
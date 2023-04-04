class Interval:
    def __init__(self,date_start,date_end):
        self.__date_start = date_start
        self.__date_end = date_end
    
    def get_start_time (self):
        return self.__date_start
    
    def get_end_time (self):
        return self.__date_end
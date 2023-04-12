from pydantic import BaseModel

class AvalibleDTO(BaseModel):
    start_date : str
    start_time : str
    end_date : str
    end_time : str
    
class BookingDTO(BaseModel):
    car : str
    start_date : str
    start_time : str
    end_date : str
    end_time : str
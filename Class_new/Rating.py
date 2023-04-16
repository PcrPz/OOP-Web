class Rating:
    def __init__(self,rating_review,rating_comment): 
        self.__rating_review = rating_review
        self.__rating_comment = rating_comment
        
    def get_rating_review (self):
        return self.__rating_review
    
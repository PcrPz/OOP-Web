from datetime import datetime
# self._check = True
    
#     def checktime_car(self,start,amount):
#         self._avalible = []
#         for i in self._car_lists:
#             for j in range(amount):
#                 date = start + datetime.timedelta(days=j)
#                 if date in i._date_not_avalible:
#                     self._check= False
#                     break
#             if self._check == True :
#                 self._avalible.append(i)
#             self._check =True

start_date= "19-6-2023"
start_time=  "12:30"
end_date= "19-7-2023"
end_time=  "12:30"
date1 = datetime.strptime(start_date + " " + start_time, '%d-%m-%Y %H:%M')
date2 = datetime.strptime(end_date + " " + end_time, '%d-%m-%Y %H:%M')


print(date1)
print(date2)
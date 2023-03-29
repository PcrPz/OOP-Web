class Contact:
    def __init__(self,contact_name,contact_username,contact_phone_num,contact_password,contact_email,contact_about,driver_license_status,contact_age_check):
        self._contact_name= contact_name
        self._contact_username = contact_username
        self._contact_phone_num = contact_phone_num
        self._contact_password = contact_password
        self._contact_email = contact_email
        self._contact_about = contact_about
        self._driver_license_status = driver_license_status
        self._contact_age_check= contact_age_check
        
class Owner(Contact):
    def __init__(self, contact_name, contact_username, contact_phone_num, contact_password, contact_email, contact_about, driver_license_status, contact_age_check,car_detail):
        super().__init__(contact_name, contact_username, contact_phone_num, contact_password, contact_email, contact_about, driver_license_status, contact_age_check)
        self.__car_detail = car_detail
        
class Renter(Contact):
    def __init__(self, contact_name, contact_username, contact_phone_num, contact_password, contact_email, contact_about, driver_license_status, contact_age_check):
        super().__init__(contact_name, contact_username, contact_phone_num, contact_password, contact_email, contact_about, driver_license_status, contact_age_check)
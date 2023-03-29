class Account:
    def __init__(self, fname, lname, username, password):
        self.fname = fname
        self.lname = lname
        self.username = username
        self.password = password

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

class Signup_login:
    def signup(self):
        new_username = input("Enter your username: ")
        while new_username in [user.get_username() for user in users]:
            new_username = input("Username used please enter new username: ")
        password = ""
        while len(password) < 4:
            password = input("Choose atleast 4 character password: ")
        fname = input("Enter your first name: ")
        lname = input("Enter your last name: ")

        user = Account(fname, lname, new_username, password)
        print("Signup success "+ user.get_username())
        users.append(user)


    def login(self):
        entry_username = ""
        while entry_username not in [user.get_username() for user in users]:
            entry_username = input("Enter your username: ")

        for user in users:
            if user.get_username() == entry_username:
                password_count = 0
                entry_password = ""
                while entry_password != user.get_password() and password_count < 3:
                    entry_password = input("Enter your password: ")
                    password_count += 1
                if entry_password == user.get_password():
                    print("Login success")
                    return
                else:
                    print("Login attempt exceeded.")
                    return

    def start(self):
        self.signup()
        self.login()

users = []
signup_login = Signup_login()
signup_login.start()
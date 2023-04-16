from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    password: str
    first_name: str = None
    last_name: str = None

class SignupLogin:
    def __init__(self):
        self.users = []

    def is_username_taken(self, username):
        for user in self.users:
            if user.username == username:
                return True
        return False

    def add_user(self, user):
        if self.is_username_taken(user.username):
            return False
        self.users.append(user)
        return True

    def is_valid_user(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return True
        return False

signup_login_system = SignupLogin()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/signup", status_code=201)
async def signup(user: User):
    if signup_login_system.add_user(user):
        return {"message": "Signup successful."}
    else:
        return {"message": "Username already taken."}

@app.post("/login", status_code=200)
async def login(username: str, password: str):
    if signup_login_system.is_valid_user(username, password):
        return {"message": "Login successful."}
    else:
        return {"message": "Invalid username or password"}

from pip import List
from uuid import uuid4
from fastapi import FastAPI
from models import User, Gender, Role


app = FastAPI()

db: List[User] = [
    User(
    id = uuid4(),
    first_name="Tatheer",
    last_name="Hussain",
    email="teting@gmail.com",
    gender=Gender.male,
    mobile = "1234567890",
    password = "123456",
    roles=[Role.admin, Role.user]
    
),
User(
    id = uuid4(),
    first_name="Shazia",
    last_name="Issac",
    email="testing2@gmail.com",
    gender=Gender.female,
    roles=[Role.user],
    password = "123456",
    mobile = "1234567890"
    
)
   
]




@app.get("/")
async def root():
    return {"Hello": "Tatheer @ Aharbal.in"}


@app.get("/api/v1/users")
async def fetch_users():
    return db;

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}
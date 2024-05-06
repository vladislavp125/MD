from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import date

app = FastAPI()


class User(BaseModel):
    id: int
    username: str
    wallet: float
    birthdate: str


db_users = [
    {"id": 1, "username": "user1", "wallet": 100.0, "birthdate": "1990-1-1"},
    {"id": 2, "username": "user2", "wallet": 200.0, "birthdate": "1995-5-15"},
]


@app.get("/users", response_model=List[User], tags=["Users"])
async def get_all_users():
    return db_users


@app.get("/users/{user_id}", response_model=User, tags=["Users"])
async def get_user(user_id: int):
    user = next((user for user in db_users if user["id"] == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.post("/users", response_model=User, tags=["Users"])
async def create_user(user: User):
    db_users.append(user.dict())
    return user


@app.put("/users/{user_id}", response_model=User, tags=["Users"])
async def update_user(user_id: int, user: User):
    for u in db_users:
        if u["id"] == user_id:
            u.update(user.dict())
            return user



@app.delete("/users/{user_id}", tags=["Users"])
async def delete_user(user_id: int):
    global db_users
    db_users = [user for user in db_users if user["id"] != user_id]
    return {"message": "Пользователь удален!"}




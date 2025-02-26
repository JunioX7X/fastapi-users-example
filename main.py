from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
users = []

class User(BaseModel):
    name: str
    email: str

@app.post("/users")
def create_user(user: User):
    users.append(user.dict())
    return {"message": "Usuario creado exitosamente"}
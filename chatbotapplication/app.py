from fastapi import FastAPI
from pydantic import BaseModel
from main import chatbot
from fastapi.middleware.cors import CORSMiddleware

api = FastAPI()

api.add_middleware(
    CORSMiddleware,
    allow_origins = ("http://127.0.0.1:8000"),
    allow_methods = ["post"],
    allow_headers = ["*"],
    allow_credentials=True
)

class UserModel(BaseModel):
    message:str


@api.post("/chatbot")
def chatbotApplication(data:UserModel):
    response = chatbot(data.message)
    return {response}

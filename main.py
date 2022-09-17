from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
    username: str
    empSatisfaction: float
    email: str
    score: int

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/")
async def read_root(item: Item): # item is posted value
    print(item)
    return {"Hello": "World"}


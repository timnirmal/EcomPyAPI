from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Optional

from Customer_Recommadation.main import func, func2, recommendation, CartItems, products
from Chat_bot.chatbot_interface import chat
from Customer_Segmentation.main import segmentation
from User_Interactions.main import productInteraction

print(func())

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    username: str
    empSatisfaction: float
    email: str
    score: int


class personID(BaseModel):
    id: int


class messageSchema(BaseModel):
    message: str


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/")
async def read_root(item: Item):  # item is posted value
    print(item)
    return {"Hello": "World"}


# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Optional[str] = None):
#    return {"item_id": item_id, "q": q}


@app.get("/recommendation")
async def Recommendation_item(person_id: personID):
    return recommendation(person_id)


@app.get("/recommendation/{id}")
async def Recommendation_item(id: int):
    print(id)
    return recommendation(id)


@app.get("/segmentation")
async def Segmentation():
    return segmentation()


@app.get("/products")
async def Recommendation_item():
    return products()


@app.get("/cart/{id}")
async def Cart_items(id: str):
    print(id)
    return CartItems(id)


@app.get("/chat")
async def Recommendation_item(message: messageSchema):
    return chat(message.message)


@app.get("/productinteractions/{id}")
async def Product_Interactions(id: int):
    print(id)
    return productInteraction(id)
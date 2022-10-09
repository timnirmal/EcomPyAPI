from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Optional

from Customer_Recommadation.main import func, func2, recommendation, CartItems, products
from Chat_bot.chatbot_interface import chat
from Customer_Segmentation.main import segmentation
from User_Interactions.main import productInteraction
from Middleware.main import userdata, search
from Sales.main import lastOrdersReport, NumofDaysSalesReport, plotData, getSalesData

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


@app.get("/user/{id}")
async def User_data(id):
    return userdata(id)


## Product Search API
#                                     name: name,
#                                     brand: brand,
#                                     priceMin: priceMin,
#                                     priceMax: priceMax,
#                                     rating: rating,
#                                     color: color,
#                                     gender: gender
#                                     category: category
@app.get("/search")
async def Search(name: str = "", brand: str = "", priceMin: float = 0.0, priceMax: float = 999999.99,
                 rating: float = 0.0, color: str = "", gender: str = "", category: str = ""):
    return search(name, brand, priceMin, priceMax, rating, color, gender, category)


@app.get("/search/{name}")
async def searchByName(name):
    return searchbyname(name)


@app.get("/search/{category}")
async def searchByCategory(category):
    return searchbycategory(category)


@app.get("/salesnum/{numoforders}")
async def salesByNumber(numoforders):
    return lastOrdersReport(int(numoforders))


# Data
@app.get("/sales/{numofdays}")
async def salesByDays(numofdays):
    return getSalesData(int(numofdays))


# Plot
@app.get("/sales/{numofdays}/plot")
async def salesByDays(numofdays):
    numofdays = 30
    return plotData(numofdays=int(numofdays))

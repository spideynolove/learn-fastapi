from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


# with path param
@app.put("/items/{item_id}")
async def create_iitem(item_id: int, item: Item):
    # item is request body
    return {"item_id": item_id, **item.dict()}


# with path + query param
@app.put("/itemms/{item_id}")   # path param in here
async def createe_item(item_id: int, item: Item, q: str | None = None, p: int | None = None):   # path + query params
    result = {"item_id": item_id, **item.dict()}
    if q and p:
        result.update({"q": q, "p": p})
    return result   # request body

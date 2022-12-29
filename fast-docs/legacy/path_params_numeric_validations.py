# from typing import Union

# from fastapi import FastAPI, Path, Query

# app = FastAPI()


# @app.get("/items/{item_id}")
# async def read_items(
#     item_id: int = Path(title="The ID of the item to get"),
#     # item_id: int = Path(default=None, alias="item-path"),
#     # item_id: Union[str, None] = None,
#     q: Union[str, None] = Query(default=None, alias="item-query"),
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results


# # ------------------------------------------------------------------------
# from datetime import datetime
# from fastapi import FastAPI, Path

# app = FastAPI()


# @app.get("/items/{item_id}")
# # async def read_items(item_id: int = Path(title="The ID of the item to get"), t: datetime = datetime.day, q: str = None):
# async def read_items(t: datetime, q: str, item_id: int = Path(title="The ID of the item to get")):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q, "time": t.date})
#     return results


# # ------------------------------------------------------------------------
from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(*, item_id: int = Path(title="The ID of the item to get"), q: str):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

from typing import List
from fastapi import APIRouter, Query
from pydantic import BaseModel

router = APIRouter()


class Item(BaseModel):
    id: int
    name: str
    price: float


items_db: List[Item] = []


@router.get("/")
async def read_root():
    return {"Hello": "World"}


@router.get("/items/{item_id}")
async def get_item(
    item_id: int,
    query_string: str | None = Query(None, alias="item-query"),
):
    for item in items_db:
        if item.id == item_id:
            return {"item_id": item.id, "q": query_string}
    return {"item_id": "not found", "q": query_string}


@router.post("/items")
async def create_item(item: Item):
    items_db.append(item)
    return item

from typing import Dict, List, Type
from fastapi import APIRouter, Query
from pydantic import BaseModel

router = APIRouter()


class IDGenerator:
    def __init__(self, models: list[Type[BaseModel]]):
        self._counters: Dict[str, int] = {model.__name__: 0 for model in models}

    def next_id(self, model: Type[BaseModel]) -> int:
        model_name = model.__name__
        if model_name not in self._counters:
            raise ValueError(
                f"Model {model_name} is not registered with this IDGenerator"
            )
        self._counters[model_name] += 1
        return self._counters[model_name]


class Item(BaseModel):
    id: int
    name: str
    price: float


id_generator = IDGenerator([Item])
items_db: List[Item] = []


@router.get("/")
def read_root():
    return {"Hello": "World"}


@router.get("/items/{item_id}")
def get_item(
    item_id: int,
    query_string: str | None = Query(None, alias="item-query"),
):
    return {"item_id": item_id, "q": query_string}


@router.post("/items")
def create_item(item: Item):
    new_id = id_generator.next_id(Item)
    new_item = Item(new_id, **item.model_dump(exclude_unset=True))
    items_db.append(new_item)
    return new_item

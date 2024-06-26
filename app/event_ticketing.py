from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Event(BaseModel):
    pass

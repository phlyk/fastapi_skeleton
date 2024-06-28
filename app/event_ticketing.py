from fastapi import APIRouter
from pydantic import BaseModel

from app.reference_endpoints import IDGenerator

router = APIRouter()


class Event(BaseModel):
    pass


id_generator = IDGenerator([Event])

from pydantic import BaseModel
from enum import Enum


class Item(Enum):
    VEG = "vegetariano"
    CARNE = "carne"
    FRANGO = "frango"

class Order(BaseModel):
    item: Item
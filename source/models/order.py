import time
from bunnet import Document as BunnetDocument, Link as BunnetLink
from beanie import Document as BeanieDocument, Link as BeanieLink
from pydantic import BaseModel
from typing import Optional
from .config import ConfigBeanie , ConfigBunnet


# ------------ My customs modus ------------ #
from .base import BaseModel


class OrderModel(BaseModel):
    create_time: int = int(time.time())
    start_time : int | None
    end_time : int | None
    status : str | None
    name : str | None



class DocumentOrder(OrderModel):
    class Settings:
        use_revision = False
        name: str = "_order"


class OrderBunnet(DocumentOrder, BunnetDocument):
    config : Optional[BunnetLink[ConfigBunnet]] = None



class OrderBeanie(DocumentOrder, BeanieDocument):
    config : Optional[BeanieLink[ConfigBeanie]] = None


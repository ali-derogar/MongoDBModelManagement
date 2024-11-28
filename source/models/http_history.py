import time
from bunnet import Document as BunnetDocument, Link as BunnetLink
from beanie import Document as BeanieDocument, Link as BeanieLink
from pydantic import BaseModel
from typing import Optional


# ------------ My customs modus ------------ #
from .base import BaseModel
from .order import OrderBeanie , OrderBunnet


class HttpHistoryModel(BaseModel):
    
    appropriate : Optional[bool] = False
    name : str | None
    method : str | None
    data_type : str | None
    create_time: int = int(time.time())
    url : str | None
    params : str | None
    redirected_from : str | None
    redirected_to : str | None
    request_header : dict | None
    request_body : dict | None
    response_body : dict | None
    



class DocumentHttpHistory(HttpHistoryModel):
    class Settings:
        use_revision = False
        name: str = "_http_history"


class HttpHistoryBunnet(DocumentHttpHistory, BunnetDocument):
    order: Optional[BunnetLink[OrderBunnet]] = None



class HttpHistoryBeanie(DocumentHttpHistory, BeanieDocument):
    order: Optional[BeanieLink[OrderBeanie]] = None

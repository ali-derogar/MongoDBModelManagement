import time
from bunnet import Document as BunnetDocument, Link as BunnetLink
from beanie import Document as BeanieDocument, Link as BeanieLink
from pydantic import BaseModel
from typing import Optional
from .config import ConfigBeanie , ConfigBunnet


# ------------ My customs modus ------------ #
from .base import BaseModel


class ReportsModel(BaseModel):
    name : str
    create_time: int = int(time.time())
    success : dict | None
    error : dict | None
    failed : dict | None

class DocumentReports(ReportsModel):
    class Settings:
        use_revision = False
        name: str = "_reports"


class ReportsBunnet(DocumentReports, BunnetDocument):
    config : Optional[BunnetLink[ConfigBunnet]] = None



class ReportsBeanie(DocumentReports, BeanieDocument):
    config : Optional[BeanieLink[ConfigBeanie]] = None


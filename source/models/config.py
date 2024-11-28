import time
from bunnet import Document as BunnetDocument, Link as BunnetLink
from beanie import Document as BeanieDocument, Link as BeanieLink
from pydantic import BaseModel
from typing import Optional
from .account import AccountBeanie, AccountBunnet


# ------------ My customs modus ------------ #
from .user import UserBunnet, UserBeanie

class Scope(BaseModel):
    add_to_cart: bool | None = None
    checkout: bool | None = None
    view_product: bool | None = None
    search_products: bool | None = None
    apply_coupon: bool | None = None
    write_review: bool | None = None
    save_for_later: bool | None = None
    track_order: bool | None = None
    return_item: bool | None = None
    contact_support: bool | None = None
    wishlist: bool | None = None
    compare_products: bool | None = None
    view_order_history: bool | None = None
    leave_feedback: bool | None = None
    subscribe_newsletter: bool | None = None


class ConfigModel(BaseModel):
    appropriate : bool = False
    create_time: int = int(time.time())
    actions : Optional[Scope] = None
    start_time : Optional[int] = None

class DocumentConfig(ConfigModel):
    class Settings:
        use_revision = False
        name: str = "_config"


class ConfigBunnet(DocumentConfig, BunnetDocument):
    user: Optional[BunnetLink[UserBunnet]] = None
    account: Optional[BunnetLink[AccountBunnet]] = None


class ConfigBeanie(DocumentConfig, BeanieDocument):
    user: Optional[BeanieLink[UserBeanie]] = None
    account: Optional[BeanieLink[AccountBeanie]] = None

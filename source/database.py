from .models import (
    UserBeanie,
    UserBunnet,
    AccountBeanie,
    AccountBunnet,
    Data,
    Information,
    Scope,
    ConfigBeanie,
    ConfigBunnet,
    OrderBeanie,
    OrderBunnet,
    HttpHistoryBeanie,
    HttpHistoryBunnet,
    ReportsBeanie,
    ReportsBunnet
)
from .initialize import initialize_beanie, initialize_bunnet


class Database:
    """
    Database is a utility class for selecting Object-Document Mapping (ODM) classes based on platform and ODM names.

    Args:
        odm_name (str): The name of the ODM (e.g., "bunnet" or "beanie").
        platform_name (str): The name of the platform (default is "instagram").

    Raises:
        ValueError: If an invalid ODM or platform name is provided.

    Example:
    >>> selector = Database("bunnet","instagram")
    >>> selector("User")
    >>> selector["User"]
    >>> selector.User

    Methods:
        __call__(class_name: str) -> Type[ODMModel]:
            Get the selected ODM class based on its name.

        __getitem__(class_name: str) -> Type[ODMModel]:
            Get the selected ODM class based on its name.

    """

    def __init__(self, odm_name: str, platform_name: str = "instagram"):
        match platform_name:
            case "Main":
                self.Scope = Scope
                self.Data = Data
                self.Information = Information
                
                if odm_name == "bunnet":
                    self.User = UserBunnet
                    self.Account = AccountBunnet
                    self.init_database = initialize_bunnet

                elif odm_name == "beanie":
                    self.User = UserBeanie
                    self.Account = AccountBeanie
                    self.init_database = initialize_beanie
                else:
                    raise ValueError("Invalid ODM name")

                self.document_models_ig = [
                    self.Account,
                ]
            case "Public":
                pass

            case "User1":
                if odm_name == "bunnet":
                    self.Config = ConfigBunnet
                    self.Order = OrderBunnet
                    self.HttpHistory = HttpHistoryBunnet
                    self.Reports = ReportsBunnet

                    self.init_database = initialize_bunnet

                elif odm_name == "beanie":
                    self.Config = ConfigBeanie
                    self.Order = OrderBeanie
                    self.HttpHistory = HttpHistoryBeanie
                    self.Reports = ReportsBeanie

                    self.init_database = initialize_beanie

                self.document_models_ = [
                    self.Config,
                    self.Order,
                    self.Reports,
                    self.HttpHistory
                ]

            case _:
                raise ValueError("Invalid platform name")

    def __call__(self, class_name: str):
        return getattr(self, class_name, "Unknown")

    def __getitem__(self, class_name: str):
        return getattr(self, class_name, "Unknown")

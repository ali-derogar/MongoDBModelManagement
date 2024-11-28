import asyncio

from database import Database


database = Database("bunnet")
User = database.User
Account = database.Account
document_models = [User, Account]


def generate_user_1():
    """
    Generate and insert a new user using Bunnet.
    """
    new_user = User(
        name="khalil", family="Abas", phone="09124870365", password="123A45678"
    )
    new_user.insert()
    print("Bunnet User ID:", new_user.id)


async def generate_user_2():
    """
    Generate and insert a new user using Beanie.
    """
    new_user = User(
        name="khalil", family="Abas", phone="09124870365", password="123A45678"
    )
    await new_user.insert()
    print("Beanie User ID:", new_user.id)


def generate_account():
    """
    Generate and insert a new account using the selected framework.
    """
    account_1 = Account(owner="6535199d0406d3f74e3de5bd")
    account_1.insert()
    print("Account ID:", account_1.id)


async def testing_beanie():
    """
    Test Beanie framework by initializing it and generating a user.
    """
    await database.init_database("mongodb://localhost:27017", "DBModelManagement",database.document_models)
    await generate_user_2()


def testing_bunnet():
    """
    Test Bunnet framework by initializing it and generating a user and an account.
    """
    database.init_database("mongodb://localhost:27017", "DBModelManagement",database.document_models)
    generate_user_1()
    generate_account()


if __name__ == "__main__":
    # Choose between testing Beanie or Bunnet based on your desired framework
    asyncio.run(testing_beanie())
    testing_bunnet()

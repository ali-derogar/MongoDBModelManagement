# Data Access Layer 

This utility class simplifies the process of selecting the appropriate ODM classes based on your project's needs.

The `Database` class is a utility for selecting Object-Document Mapping (ODM) classes based on the chosen platform and ODM names. It simplifies the process of accessing the right ODM classes for different platforms and database models.

## Importing

You need to import the necessary ODM classes from your models and instantiate the `Database` class with the chosen ODM name and platform. Then you can easily access the desired ODM class using the `Database` instance.

```python
from database import Database
```
## Usage

The `Database` class can be initialized with the following parameters:

- `odm_name` : The name of the ODM type, either "bunnet" or "beanie."
- `platform_name` : The name of the platform, with "instagram" as the default.

Example:

```python
# Initialize the Database selector for the "bunnet" ODM on the "instagram" platform.
selector = Database("bunnet", "instagram")
selector.init_database("mongodb://localhost:27017", "DBModelManagement",selector.document_models)

# Access the ODM class for "User" using different methods.
User = selector("User") 
User = selector["User"]  
User = selector.User  

Account = databases.Account
```

## Supported Platforms and ODM Types

The `Database` class currently supports the following platforms and ODM types:

### Platform: Instagram

- ODM Type: **Bunnet** & **Beanie**

  -  User
  -  Account
  -  Config
  -  Order
  -  HttpHistory
  -  Reports

### Platform: Main
- Support for Main platform can be added here if needed.

### Platform: User1
- Support for User1 platform can be added here if needed.

## Error

The `Database` class raises a `ValueError` when an invalid platform or ODM type name is provided. This ensures that only valid selections are made.

## Example

```python
selector = Database("bunnet", "User1")
User = selector.User
...
```
# plusoft-api

Use Edusense API funcionalities in your python application.

## Instalation
```sh
pip install plusoft-api
```

## Usage Examples
You can use this package in order to access [Edusense API Rest Api Methods](https://edusense.docs.apiary.io/#introduction/overview/requisicoes).

First one, you need to instantiate the PlusoftApi object, by passing your username, password and domain:
```python
from plusoft_api import PlusoftApi


# We recommend the use of environment variables to improve security to your credentials
plusoft_api = PlusoftApi(
    username="your-login",
    password="your-password",
    domain="your-domain" # You can get this in your environment url, for example: https://{your-domain}.edusense.app
)
```

After that, you can access the api methods, for example to insert new users:
```python
from plusoft_api import PlusoftApi


# We recommend the use of environment variables to improve security to your credentials
plusoft_api = PlusoftApi(
    username="your-login",
    password="your-password",
    domain="your-domain" # You can get this in your environment url, for example: https://{your-domain}.edusense.app
)

users = [
    {"login": "user1", "name": "User 1", "email": "user1@gmail.com"},
    {"login": "user2", "name": "User 2", "email": "user2@gmail.com"},
    {"login": "user3", "name": "User 3", "email": "user3@gmail.com"},
    {"login": "user4", "name": "User 4", "email": "user4@gmail.com"}
]

for user in users:
    plusoft_api.users.insert_users.add_to_payload(**user) # This method will check and store in memory the user to use later to generate payload and upload to plusoft

plusoft_api.users.insert_users.upload() # This method will upload to plusoft the users stored by add_to_payload method
```

_**This library is under development and not all methods are available.**_

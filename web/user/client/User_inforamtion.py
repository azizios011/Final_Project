# user/client/users_information.py
from .base import ClientBase

class UserInformation(ClientBase):
    def __init__(self, username, email, customer_info):
        super().__init__(username, email, customer_info)

    def get_user_information(self):
        return {
            "username": self.username,
            "email": self.email,
            "customer_info": self.customer_info
        }

    def login(self, username, password):
        # Forward the login information to the base class for handling
        return self.base_login(username, password)

    def signup(self, username, email, customer_info):
        # Forward the signup information to the base class for handling
        return self.base_signup(username, email, customer_info)

    # Other methods specific to user information

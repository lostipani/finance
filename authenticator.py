import os

class AuthenticatorBase:
    pass

class AuthenticatorToken(AuthenticatorBase):

    def __init__(self, token: str=None):
        self.token = token if token else os.environ.get("TOKEN")        

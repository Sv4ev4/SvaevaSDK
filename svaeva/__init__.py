from typing import Any
from requests import Session

from dotenv import load_dotenv


from svaeva.Paths.Actions    import Actions 
from svaeva.Paths.Present    import PresentModels
from svaeva.Paths.Platform   import Platforms
from svaeva.Paths.Group      import Groups
from svaeva.Paths.User       import Users

import os

class InvalidToken(Exception):
    def __init__(self, token, message="Invalid token"):
        self.token = token
        self.message = f'{message}: {token}'
        super().__init__(self.message)

class Svaeva:

    conn  : Session
    token : str

    present  = PresentModels
    platform = Platforms
    group    = Groups
    users    = Users
    actions  = Actions

    end : str

    def __init__(self,api_key : str,end_point="http://127.0.0.1:8000") -> None:
        load_dotenv()
        # Set The Golbal Varibles
        self.token = api_key
        self.conn  = Session()
        # Check
        self.end_point(end_point)
        self.set_headres
        self.check

    def end_point(self,end_):
        # Set
        token = os.getenv("KEY_SVAEVA")
        if token is not None:
            self.token  = token
        end   = os.getenv("URL_SVAEVA")
        if end is not None:
            self.end = end
        else:
            self.end = end_


    @property
    def set_headres(self):
        self.conn.headers.update({
            "token":self.token,
            "accept": "application/json"
        })

    @property
    def check(self) -> None:
        response = self.conn.get(f"{self.end}/")
        if response.status_code == 200:
            self.present  = self.present(self.conn,self.end)
            self.platform = self.platform(self.conn,self.end)
            self.group    = self.group(self.conn, self.end)
            self.users    = self.users(self.conn, self.end)
            self.actions  = self.actions(self.conn, self.end)
            return True
        raise InvalidToken(self.token)


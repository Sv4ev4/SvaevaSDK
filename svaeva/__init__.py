import logging
from typing import Any
from requests import Session
from dotenv import load_dotenv

from svaeva.Paths.Actions import Actions 
from svaeva.Paths.Present import PresentModels
from svaeva.Paths.Platform import Platforms
from svaeva.Paths.Group import Groups
from svaeva.Paths.User import Users

import os

# Setting up logging
logging.basicConfig(filename='svaeva.log',level=logging.INFO)

class InvalidToken(Exception):
    def __init__(self, token, message="Invalid token"):
        self.token = token
        self.message = f'{message}: {token}'
        super().__init__(self.message)

class Svaeva:

    def __init__(self,api_key : str,end_point_="http://127.0.0.1:8000") -> None:
        load_dotenv()
        # Set The Global Variables
        self.token = api_key
        self.conn  = Session()
        # Check
        self.end_point(end_point_)
        self.set_headres
        self.check
    def end_point(self, end_):
        # Set
        token = os.getenv("KEY_SVAEVA")
        if token is not None:
            self.token = token
            logging.info(f"Environment variable KEY_SVAEVA: {token}")
        else:
            logging.warning("Environment variable KEY_SVAEVA not found.")
        end = os.getenv("URL_SVAEVA")
        if end is not None:
            self.end = end
            logging.info(f"Environment variable URL_SVAEVA: {end}")
        else:
            self.end = end_
            logging.warning("Environment variable URL_SVAEVA not found, using default.")

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
            logging.info("Connection established successfully.")
            self.present  = PresentModels(self.conn,self.end)
            self.platform = Platforms(self.conn,self.end)
            self.group    = Groups(self.conn, self.end)
            self.users    = Users(self.conn, self.end)
            self.actions  = Actions(self.conn, self.end)
            return True
        logging.error("Connection failed. Invalid token.")
        raise InvalidToken(self.token)



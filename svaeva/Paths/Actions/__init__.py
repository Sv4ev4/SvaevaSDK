from typing import Any, Dict
from requests import Session

# Custom exception for when the user is empty
class UserIsEmpty(Exception):
    def __init__(self, message="The user is empty"):
        self.message = message
        super().__init__(self.message)

# Custom exception for invalid user ID
class InvalidUserID(Exception):
    def __init__(self, message="Invalid user ID"):
        self.message = message
        super().__init__(self.message)

# Custom exception for error in setting user
class ErrorSettingUser(Exception):
    def __init__(self, message=""):
        self.message = message
        super().__init__(self.message)

class Actions:
    # Initialize with connection and endpoint
    def __init__(self, conn: Session, end_point: str):
        self.conn = conn
        self.url = f"{end_point}/v1/db/action/"

    # Call method to get all users
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        if isinstance(args, Dict):
            try:
                data = self.conn.get(self.url,params=args)
                if data.status_code == 200:
                    return data.json()
                if data.json()["detail"] == 'Not Found':
                    raise UserIsEmpty()
            except Exception as e:
                raise e
        else:
            try:
                data = self.conn.get(self.url)
                if data.status_code == 200:
                    return data.json()
                if data.json()["detail"] == 'Not Found':
                    raise UserIsEmpty()
            except Exception as e:
                raise e
    
    # Get a specific user by name
    def __getattr__(self, name):
        if name in self.__dict__:
            return self.__dict__[name]
        else:
            try:
                data = self.conn.get(self.url, params={"id":name})
                if data.status_code == 200:
                    self.__dict__[name] = data.json()
                    return self.__dict__[name]
                else:
                    raise InvalidUserID()
            except Exception as e:
                raise e

    # Set a user
    def __setattr__(self, name, value):
        if name not in ['conn', 'url']:
            value.update({"id":name})
            try:
                data = self.conn.post(self.url, json=value)
                if data.status_code != 200:
                    raise ErrorSettingUser(data.json())
                self.__dict__[name] = value  
            except Exception as e:
                raise e
        else:
            self.__dict__[name] = value
        return None
    
    # Update a user
    def update(self, **kwargs):
        try:
            self.conn.put(self.url, params=kwargs["id"], json=kwargs)
        except Exception as e:
            raise e
        
    @property
    def loaded(self):
        return [_ for _ in self.__dict__ if _ not in ['conn', 'url']]

    # Delete a user
    def __delattr__(self, name):
        try:
            self.conn.delete(self.url, params={"id":name})
        except Exception as e:
            raise e
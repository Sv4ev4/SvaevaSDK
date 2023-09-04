from typing import Any
from requests import Session

# Custom exception for when the platform is empty
class PlatformIsEmpty(Exception):
    def __init__(self, message="The platform is empty"):
        self.message = message
        super().__init__(self.message)

# Custom exception for invalid platform ID
class InvalidPlatformID(Exception):
    def __init__(self, message="Invalid platform ID"):
        self.message = message
        super().__init__(self.message)

# Custom exception for error in setting platform
class ErrorSettingPlatform(Exception):
    def __init__(self, message=""):
        self.message = message
        super().__init__(self.message)

class Groups:
    # Initialize with connection and endpoint
    def __init__(self, conn: Session, end_point: str):
        self.conn = conn
        self.url = f"{end_point}/v1/db/group/"

    # Call method to get all platforms
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        try:
            data = self.conn.get(self.url)
            if data.status_code == 200:
                return data.json()
            print(data)
            if data.json()["detail"] == 'Not Found':
                raise PlatformIsEmpty()
        except Exception as e:
            raise e
    
    # Get a specific platform by name
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
                    raise InvalidPlatformID()
            except Exception as e:
                raise e

    # Set a platform
    def __setattr__(self, name, value):
        if name not in ['conn', 'url']:
            value.update({"id":name})
            try:
                data = self.conn.post(self.url, json=value)
                if data.status_code != 200:
                    raise ErrorSettingPlatform(data.json())
                self.__dict__[name] = value  
            except Exception as e:
                raise e
        else:
            self.__dict__[name] = value
        return None
    
    # Update a platform
    def update(self, **kwargs):
        try:
            self.conn.put(self.url, params=kwargs["id"], body=kwargs)
        except Exception as e:
            raise e
        
    @property
    def loaded(self):
        return [_ for _ in self.__dict__ if _ not in ['conn', 'url']]

    # Delete a platform
    def __delattr__(self, name):
        try:
            self.conn.delete(self.url, params={"id":name})
        except Exception as e:
            raise e

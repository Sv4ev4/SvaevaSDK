from typing import Any
from requests import Session

# Custom exception for when the present is empty
class PresentIsEmpty(Exception):
    def __init__(self, message="The present is empty"):
        self.message = message
        super().__init__(self.message)

# Custom exception for invalid present model ID
class InvalidPresentModelID(Exception):
    def __init__(self, message="Invalid present model ID"):
        self.message = message
        super().__init__(self.message)

# Custom exception for error in setting present model
class ErrorSettingPresentModel(Exception):
    def __init__(self, message=""):
        self.message = message
        super().__init__(self.message)

class PresentModels:
    # Initialize with connection and endpoint
    def __init__(self, conn: Session, end_point: str):
        self.conn = conn
        self.url = f"{end_point}/v1/db/presentmodels/"

    # Call method to get all present models
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        try:
            data = self.conn.get(self.url)
            if data.status_code == 200:
                return data.json()
            if data.json()["detail"] == 'Not Found':
                raise PresentIsEmpty()
        except Exception as e:
            raise e
    
    # Get a specific present model by name
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
                    raise InvalidPresentModelID()
            except Exception as e:
                raise e

    # Set a present model
    def __setattr__(self, name, value):
        if name not in ['conn', 'url']:
            value.update({"id":name})
            try:
                data = self.conn.post(self.url, json=value)
                if data.status_code != 200:
                    raise ErrorSettingPresentModel(data.json())
                self.__dict__[name] = value  
            except Exception as e:
                raise e
        else:
            self.__dict__[name] = value
        return None
    
    # Update a present model
    def update(self, **kwargs):
        try:
            self.conn.put(self.url, json={"item_id":kwargs["id"], "item":kwargs})
        except Exception as e:
            raise e
        
    @property
    def loaded(self):
        return [_ for _ in self.__dict__ if _ not in ['conn', 'url']]

    # Delete a present model
    def __delattr__(self, name):
        try:
            self.conn.delete(self.url, params={"id":name})
        except Exception as e:
            raise e


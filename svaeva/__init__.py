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

    def end_point(self,end):
        # Set
        env_load = os.getenv("SVAEVA_KEY")
        if env_load is not None:
            end  = env_load
        # End Point
        self.end = end

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


import random

def create_random_present_model_dict():
    # Create a dictionary with the generated values
    present_model_dict = {
        'id': str(random.randint(1, 100)),
        'present_type': random.choice(['conversation', 'analysis']),
        'agent_type': 'default',
        'llm_type': 'openai',
        'model': random.choice(['gpt-1', 'gpt-2', 'gpt-3', 'gpt-4']),
        'max_tokens': random.randint(1, 100),
        'temperature': round(random.uniform(0, 1), 2),
        'presence_penalty': round(random.uniform(0, 1), 2),
        'frequency_penalty': round(random.uniform(0, 1), 2),
        'top_p': round(random.uniform(0, 1), 2),
        'top_k': random.randint(1, 10),
        'system_prompt': 'System prompt'
    }

    return present_model_dict


# Exemple

svaeva = Svaeva("a60d6079937e941411018fcd31638418ce37c555585cf949bfdfde4d1ca3c974392176eab57d64747f12852ac02822b4c840df90caab4479e010bee481697303")

# # To setted PresentModels
# svaeva.present.ola = create_random_present_model_dict()
# svaeva.present.test = create_random_present_model_dict()
# # Show all
# print(svaeva.present())
# # Show Presentmodels
# print(svaeva.present.ola)
# print(svaeva.present.test)
# # Test Error
# try:
#     print(svaeva.present.not_setted)
# except Exception as e:
#     print("Svaeva not setted pass", e)
# # Show already loaded Presentmodels
# #for _ in svaeva.present():
# #    print(_)
# #    svaeva.__delattr__(svaeva.present, _.id)
# print(svaeva.present.loaded)
# # Create Platform (platform.create.*)
# svaeva.platform.whastapp = {"pf_parms":["phone_number"]}
# # Show all platforms avalable to load
# print(svaeva.platform())
# # show Whatapp Info
# print(svaeva.platform.whastapp)
# # Show Loaded Platforms
# print(svaeva.platform.loaded)
# # Create a new group
# svaeva.group.test = {"conversation_present_id":"ola"}
# # Show all
# print(svaeva.group())
# # Show the newly created group
# print(svaeva.group.test)
# Add a user to the group
#svaeva.users.test = {"group_id": "test", "id": "abjdaijkdhujahid","platform":"whastapp","phone_number":"+351919771555"}
# Show all users
#print(svaeva.users())
# Show the user just added
#print(svaeva.users.test)
# Create a new action
svaeva.actions.test_action = {"action_id": "test_action", "action_type": "type1", "parameters": {"param1": "value1"}}
# Show all actions
print(svaeva.actions())
# Show the action just added
print(svaeva.actions.test_action)

from svaeva import Svaeva

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

svaeva = Svaeva("a60d6079937e941411018fcd31638418ce37c555585cf949bfdfde4d1ca3c974392176eab57d64747f12852ac02822b4c840df90caab4479e010bee481697303","http://192.168.1.205:8000")

# To setted PresentModels
svaeva.present.ola = create_random_present_model_dict()
svaeva.present.test = create_random_present_model_dict()
# Show all
print(svaeva.present())
# Show Presentmodels
print(svaeva.present.ola)
print(svaeva.present.test)
# Test Error
try:
    print(svaeva.present.not_setted)
except Exception as e:
    print("Svaeva not setted pass", e)
# Show already loaded Presentmodels
#for _ in svaeva.present():
#    print(_)
#    svaeva.__delattr__(svaeva.present, _.id)
print(svaeva.present.loaded)
# Create Platform (platform.create.*)
svaeva.platform.whastapp = {"pf_parms":["phone_number"]}
# Show all platforms avalable to load
print(svaeva.platform())
# show Whatapp Info
print(svaeva.platform.whastapp)
# Show Loaded Platforms
print(svaeva.platform.loaded)
# Create a new group
svaeva.group.test = {"conversation_present_id":"ola"}
# Show all
print(svaeva.group())
# 
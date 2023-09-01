#--------------/-------------
# Tests and exemples


import pytest
import random
from svaeva import Svaeva

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

@pytest.fixture
def svaeva():
    return Svaeva("a60d6079937e941411018fcd31638418ce37c555585cf949bfdfde4d1ca3c974392176eab57d64747f12852ac02822b4c840df90caab4479e010bee481697303")

def test_present_models(svaeva):
    # Test setting PresentModels
    svaeva.present.ola = create_random_present_model_dict()
    svaeva.present.test = create_random_present_model_dict()

    # Test getting all PresentModels
    assert isinstance(svaeva.present(), dict)

    # Test getting specific PresentModels
    assert isinstance(svaeva.present.ola, dict)
    assert isinstance(svaeva.present.test, dict)

    # Test getting a non-set PresentModel
    with pytest.raises(Exception):
        print(svaeva.present.not_setted)

    # Test deleting and getting loaded PresentModels
    for _ in svaeva.present():
        svaeva.__delattr__(svaeva.present, _.id)
    assert isinstance(svaeva.present.loaded, dict)

def test_platform(svaeva):
    # Test creating and getting a Platform
    svaeva.platform.whastapp = {"pf_parms":["phone_number"]}
    assert isinstance(svaeva.platform(), dict)
    assert isinstance(svaeva.platform.whastapp, dict)
    assert isinstance(svaeva.platform.loaded, dict)

def test_group(svaeva):
    # Test creating and getting a Group
    svaeva.group.test = {"conversation_present_id":"ola"}
    assert isinstance(svaeva.group(), dict)
import pytest
import os
import json

@pytest.fixture(scope="session")
def config():
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")
    with open(filename)as f:
        return json.load(f)
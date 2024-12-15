import sys
import os
import pytest

# Add the directory containing main.py to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import hello_world

def test_hello_world():
    request = None  # Adjust this as needed for your specific request object
    response = hello_world(request)
    assert response == "Hello World"
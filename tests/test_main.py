import pytest
from fastapi.testclient import TestClient
from app.main import app
from models.text_model import TextModel

# Utilize a fixture for the TestClient
@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as client:
        yield client

def test_fibonacci_sequence(test_client):
    """
    Test the Fibonacci API for known inputs and outputs.
    
    This test checks if the API returns the correct Fibonacci sequence 
    for the given input numbers. It uses a parameterized test approach
    to avoid redundancy and makes the test easily extendable.
    
    Args:
        test_client (TestClient): Fixture for creating a test client for the API.
    """

    # Dictionary mapping input values to expected Fibonacci results
    test_cases = {
        0:0,
        1: 1,
        2: 1,
        3: 2,
        7: 13,
        10: 55,
        20: 6765
    }

    # Loop through the test cases to ensure code reusability
    for input_value, expected_result in test_cases.items():
        # Make the GET request to the FastAPI endpoint
        response = test_client.get(f"/{input_value}")
        
        # Check if the status code is as expected (200 OK)
        assert response.status_code == 200, f"Failed for input: {input_value}"
        
        # Check if the JSON response is the expected Fibonacci number
        assert response.json() == expected_result, f"Failed for input: {input_value}"



def test_text_sentiment(test_client):
    """
    Test the sentiment for known inputs and outputs.
    
    This test checks if the API returns the correct sentiment  
    for the given input numbers. It uses a parameterized test approach
    to avoid redundancy and makes the test easily extendable.
    
    Args:
        test_client (TestClient): Fixture for creating a test client for the API.
    """

    # Dictionary mapping input values to expected sentiment results
    test_cases = {
        "very good day": "positive",
        "food was ok but the place is too dirty": "negative",
        "Loved the food, but the money isnt worth it! Anyways, i am pretty happy :)": "positive",
        "Having a family is kool, but having friends is kooler!": "positive",
        "the day is saved by the PPG" : "positive"

    }

    # Loop through the test cases to ensure code reusability
    for input_value, expected_result in test_cases.items():
        # Make the GET request to the FastAPI endpoint
        data = {"text": input_value}
        response = test_client.post("/predict/",json=data)
        
        # Check if the status code is as expected (200 OK)
        assert response.status_code == 200, f"text Failed for input: {input_value}"
        
        # Check if the JSON response is the expected sentiment value for the input
        assert response.json() == expected_result, f"text Failed for input: {input_value}, response was {response.json()}"
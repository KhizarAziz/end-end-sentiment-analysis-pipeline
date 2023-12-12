from fastapi import FastAPI, HTTPException
from models.text_model import TextModel
from services.nlp_service import NLPService

app = FastAPI()
nlp_service = NLPService()

def fibonacci(n: int) -> int:
    """
    Calculate the n-th Fibonacci number.

    Parameters:
    n (int): The index (n) of the Fibonacci sequence to compute.

    Returns:
    int: The n-th Fibonacci number.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 0
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

@app.get("/{n}", response_model=int)
async def read_item(n: int) -> int:
    """
    Endpoint to retrieve the n-th Fibonacci number.

    Parameters:
    n (int): The index (n) of the Fibonacci sequence to retrieve.

    Responses:
    200: Return the n-th Fibonacci number.
    422: Validation error for invalid input.
    """
    try:
        return fibonacci(n)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))


@app.post("/predict/")
async def predict_text(text_model: TextModel) -> dict:
    """
    Endpoint to predict the sentiment of the given text.

    Args:
        text_model (TextModel): The input model containing the text to be analyzed.

    Returns:
        dict: A dictionary containing the prediction results.

    Raises:
        HTTPException: If an error occurs during prediction.
    """
    try:
        return nlp_service.predict(text_model.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
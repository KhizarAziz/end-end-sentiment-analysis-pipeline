from pydantic import BaseModel

class TextModel(BaseModel):
    """
    Pydantic model representing the text input for prediction.
    """
    text: str

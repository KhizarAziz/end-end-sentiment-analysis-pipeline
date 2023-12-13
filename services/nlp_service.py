from transformers import DistilBertForSequenceClassification, DistilBertTokenizer
import torch
from utils.text_utils import clean_text, tokenize
from config import config

class NLPService:
    """
    Service class for NLP-related operations.
    """

    def __init__(self):
        """
        Initializes the NLP service with necessary model and tokenizer.
        """
        self.model_name = config.SENTIMENT_MODEL
        self.tokenizer = DistilBertTokenizer.from_pretrained(self.model_name)
        self.model = DistilBertForSequenceClassification.from_pretrained(self.model_name)

    def predict(self, text: str) -> dict:
        """
        Predicts the sentiment of a given text string.

        Args:
            text (str): The input text for sentiment analysis.

        Returns:
            str: A string containing the sentiment.
        """
        cleaned_text = clean_text(text)
        tokens = tokenize(cleaned_text, self.tokenizer)
        with torch.no_grad():
            outputs = self.model(tokens)
        probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)


        # Find the sentiment with the higher probability
        probabilities = {"positive": probabilities[0][1].item(), "negative": probabilities[0][0].item()}
        sentiment = max(probabilities, key=probabilities.get)
        
        return sentiment #{"positive": probabilities[0][1].item(), "negative": probabilities[0][0].item()}

import torch
from transformers import PreTrainedTokenizer
import re

def clean_text(text: str) -> str:
    """
    Cleans the input text by removing or altering unwanted characters.

    Args:
        text (str): The input text to be cleaned.

    Returns:
        str: The cleaned text.
    """
    # Remove HTML tags
    text = re.sub(r'<.*?>', '', text)
    # Remove URLs
    text = re.sub(r'http\S+|www.\S+', '[URL]', text)
    # Remove Emails
    text = re.sub(r'\S+@\S+', '[EMAIL]', text)
    # Remove new line and line breaks
    text = text.replace('\n', ' ').replace('\r', '').strip()
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    # Optional: Lowercase (Depends on whether your DistilBERT model is cased or not)
    # text = text.lower()
    return text

def tokenize(text: str, tokenizer: PreTrainedTokenizer) -> torch.Tensor:
    """
    Tokenizes the given text using the specified tokenizer.

    Args:
        text (str): The text to tokenize.
        tokenizer (PreTrainedTokenizer): The tokenizer to use.

    Returns:
        torch.Tensor: The tokenized text as a PyTorch tensor.
    """
    return tokenizer.encode(text, return_tensors="pt",padding=True, truncation=True)

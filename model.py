# model.py

def predict_sentiment(text):
    """
    A simple sentiment analysis function that classifies text as positive, negative, or neutral.
    
    Args:
        text (str): The input text to analyze.
        
    Returns:
        str: The sentiment label ("positive", "negative", or "neutral").
    """
    # Simple keyword-based sentiment analysis

    
    if not text:
        return "neutral"
    if "happy" in text.lower() or "good" in text.lower():
        return "positive"
    if "sad" in text.lower() or "bad" in text.lower():
        return "negative"
    return "neutral"

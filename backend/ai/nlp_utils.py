import spacy
from textblob import TextBlob
from typing import Dict

nlp = spacy.load("en_core_web_sm")

def analyze_text(text: str) -> Dict:
    """Extract keywords and analyze sentiment"""
    doc = nlp(text)
    keywords = [
        token.lemma_.lower() for token in doc
        if not token.is_stop and token.pos_ in ['NOUN', 'VERB']
    ]
    sentiment = TextBlob(text).sentiment.polarity
    
    return {
        "keywords": list(set(keywords)),  # Deduplicate
        "sentiment": round(sentiment, 2)
    } 
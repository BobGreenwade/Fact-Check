"""
segmentText.py — Breaks input into sentences and extracts assertions

Supports editorial parsing, compound statement handling, and assertion tagging.
Drafted collaboratively with Copilot and Bob Greenwade.
"""

import re
import nltk
from nltk.tokenize import sent_tokenize

nltk.download("punkt", quiet=True)

def split_into_sentences(text):
    """
    Splits input text into discrete sentences using NLTK.
    Handles punctuation, conjunctions, and run-ons.
    """
    return sent_tokenize(text)

def extract_assertions(sentence):
    """
    Extracts one or more factual assertions from a sentence.
    Handles compound statements and implied claims.
    """
    parts = re.split(r"\b(?:and|but|or|so|because|although|while|however)\b", sentence, flags=re.IGNORECASE)
    assertions = [p.strip() for p in parts if len(p.strip()) > 5]
    return assertions

def tag_assertion_type(assertion):
    """
    Tags assertion as factual, speculative, opinion, or question.
    Placeholder logic; refine with ML or rule-based classifier.
    """
    speculative_keywords = ["might", "could", "possibly", "maybe", "i think", "it seems"]
    opinion_keywords = ["i believe", "in my opinion", "i feel", "should", "ought"]

    lowered = assertion.lower()
    if any(k in lowered for k in speculative_keywords):
        return "speculative"
    elif any(k in lowered for k in opinion_keywords):
        return "opinion"
    elif "?" in assertion:
        return "question"
    else:
        return "factual"

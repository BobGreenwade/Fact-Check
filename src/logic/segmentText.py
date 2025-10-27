"""
segmentText.py — Breaks input into sentences and extracts assertions

Supports editorial parsing, compound statement handling, and assertion tagging.
Now includes ML-ready assertion typing and expansion hooks.
Drafted collaboratively with Copilot and Bob Greenwade.
"""

import re
import nltk
from nltk.tokenize import sent_tokenize
from batchInvariant import run_deterministic_inference
from selectMachineLearning import ml_select_package

nltk.download("punkt", quiet=True)

def split_into_sentences(text):
    """
    Splits input text into discrete sentences using NLTK.
    Handles punctuation, conjunctions, and run-ons.
    """
    return sent_tokenize(text)

def extract_assertions(sentence):
    """
    Extracts individual assertions from compound sentence.
    Expands compound subjects into separate claims.
    """
    parts = re.split(r"\b(?:and|but|or|so|because|although|while|however)\b", sentence, flags=re.IGNORECASE)
    assertions = [p.strip() for p in parts if len(p.strip()) > 5]

    expanded = []
    for a in assertions:
        expanded.extend(expand_entity_assertions(a))
    return expanded

def tag_assertion_type(assertion):
    """
    Tags assertion as factual, speculative, opinion, or question.
    Uses keyword heuristics; future upgrade to ML classifier.
    """
    speculative_keywords = ["might", "could", "possibly", "maybe", "i think", "it seems"]
    opinion_keywords = ["i believe", "in my opinion", "i feel", "should", "ought"]
    question_keywords = ["who", "what", "why", "how", "when", "where"]

    lowered = assertion.lower()
    scores = {
        "factual": 0.85,
        "speculative": 0.0,
        "opinion": 0.0,
        "question": 0.0
    }

    for kw in speculative_keywords:
        if kw in lowered:
            scores["speculative"] += 0.2
            scores["factual"] -= 0.1
    for kw in opinion_keywords:
        if kw in lowered:
            scores["opinion"] += 0.2
            scores["factual"] -= 0.1
    for kw in question_keywords:
        if lowered.startswith(kw) or lowered.endswith("?"):
            scores["question"] += 0.5
            scores["factual"] -= 0.2

    best_type = max(scores, key=scores.get)
    return {
        "type": best_type,
        "scores": {k: round(v, 2) for k, v in scores.items()}
    }

def expand_entity_assertions(assertion):
    """
    Expands assertions with compound subjects into individual claims.
    Example: 'Charles and Camilla are reptiles' → ['Charles is a reptile', 'Camilla is a reptile']
    Placeholder logic; refine with NLP parser or dependency tree.
    """
    match = re.match(r"(.+?) and (.+?) (are|were|will be|seem to be) (.+)", assertion, re.IGNORECASE)
    if match:
        subj1, subj2, verb, predicate = match.groups()
        return [f"{subj1.strip()} {verb} {predicate}", f"{subj2.strip()} {verb} {predicate}"]
    return [assertion]

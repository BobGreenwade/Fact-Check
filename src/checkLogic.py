"""
checkLogic.py — Evaluates logical structure and consistency of assertions

Detects contradictions, fallacies, and rhetorical misdirection.
Supports editorial tagging and ML-enhanced logic scoring.
Drafted collaboratively with Copilot and Bob Greenwade.
"""

import re

# Placeholder for ML integration
def detect_fallacies(text):
    """
    Detects common logical fallacies in the input text.
    Returns a list of fallacy tags and brief explanations.
    """
    fallacies = []
    # Example stub logic
    if "everyone knows" in text.lower():
        fallacies.append(("Appeal to Popularity", "Claim relies on consensus rather than evidence."))
    if "if we don't act now" in text.lower():
        fallacies.append(("False Dilemma", "Presents only two options when more exist."))
    return fallacies

def detect_contradictions(text, known_facts):
    """
    Compares input text against known facts to flag contradictions.
    Returns contradiction tags and suggested corrections.
    """
    contradictions = []
    # Example stub logic
    for fact in known_facts:
        if fact.lower() in text.lower():
            continue
        if "not " + fact.lower() in text.lower():
            contradictions.append((fact, "Contradicts known fact."))
    return contradictions

def tag_rhetorical_misdirection(text):
    """
    Flags rhetorical devices that obscure logic (e.g., loaded language, red herrings).
    Returns editorial tags for phrasing review.
    """
    tags = []
    if "clearly" in text.lower():
        tags.append(("Loaded Language", "Implies certainty without justification."))
    if "some say" in text.lower():
        tags.append(("Vague Attribution", "Avoids source responsibility."))
    return tags

def evaluate_logic(text, known_facts=None):
    """
    Main entry point for logic evaluation.
    Returns a structured report of fallacies, contradictions, and rhetorical tags.
    """
    known_facts = known_facts or []
    return {
        "fallacies": detect_fallacies(text),
        "contradictions": detect_contradictions(text, known_facts),
        "rhetorical_tags": tag_rhetorical_misdirection(text)
    }

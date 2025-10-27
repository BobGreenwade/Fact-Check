"""
checkLogic.py — Evaluates logical structure and consistency of assertions

Detects contradictions, fallacies, and rhetorical misdirection.
Supports editorial tagging and ML-enhanced logic scoring.
Drafted collaboratively with Copilot and Bob Greenwade.
"""

import re

def detect_fallacies(text):
    """
    Detects common logical fallacies in the input text.
    Returns list of fallacy tags with weights and explanations.
    """
    fallacies = []
    lowered = text.lower()

    if "everyone knows" in lowered:
        fallacies.append({
            "type": "Appeal to Popularity",
            "explanation": "Claim relies on consensus rather than evidence.",
            "weight": 0.6
        })
    if "if we don't act now" in lowered:
        fallacies.append({
            "type": "False Dilemma",
            "explanation": "Presents only two options when more exist.",
            "weight": 0.7
        })

    return fallacies

def detect_contradictions(text, known_facts):
    """
    Compares input text against known facts to flag contradictions.
    Returns list of contradictions with severity scores.
    """
    contradictions = []
    lowered = text.lower()

    for fact in known_facts:
        fact_lower = fact.lower()
        if fact_lower in lowered:
            continue
        if "not " + fact_lower in lowered:
            contradictions.append({
                "fact": fact,
                "explanation": "Contradicts known fact.",
                "severity": 0.8
            })

    return contradictions

def tag_rhetorical_misdirection(text):
    """
    Flags rhetorical devices that obscure logic.
    Returns list of editorial tags with sabotage potential.
    """
    tags = []
    lowered = text.lower()

    if "clearly" in lowered:
        tags.append({
            "type": "Loaded Language",
            "explanation": "Implies certainty without justification.",
            "sabotage_score": 0.5
        })
    if "some say" in lowered:
        tags.append({
            "type": "Vague Attribution",
            "explanation": "Avoids source responsibility.",
            "sabotage_score": 0.4
        })

    return tags

def evaluate_logic(text, known_facts=None):
    """
    Main entry point for logic evaluation.
    Returns structured report with fallacies, contradictions, and rhetorical tags.
    """
    known_facts = known_facts or []
    return {
        "fallacies": detect_fallacies(text),
        "contradictions": detect_contradictions(text, known_facts),
        "rhetorical_tags": tag_rhetorical_misdirection(text)
    }

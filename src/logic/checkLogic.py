"""
checkLogic.py — Evaluates logical structure and consistency of assertions

Detects contradictions, fallacies, and rhetorical misdirection.
Supports editorial tagging, sabotage scoring, and ML-enhanced logic analysis.
Drafted collaboratively with Copilot and Bob Greenwade.
"""

import re
from selectMachineLearning import ml_select_package
from batchInvariant import run_deterministic_inference

# Optional ML hook for logic scoring
def score_logical_consistency(text):
    """
    Uses ML model to score logical consistency of the input.
    Placeholder: replace with actual model or scoring function.
    """
    model = ml_select_package(task="classification")
    return run_deterministic_inference(lambda x: 0.75)  # Replace with actual logic model

def detect_fallacies(text):
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
    known_facts = known_facts or []
    return {
        "fallacies": detect_fallacies(text),
        "contradictions": detect_contradictions(text, known_facts),
        "rhetorical_tags": tag_rhetorical_misdirection(text),
        "logic_score": score_logical_consistency(text)
    }

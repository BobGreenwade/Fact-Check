"""
checkFact.py — Verifies individual assertions using editorial logic and ML inference

Supports source-based verification, semantic similarity scoring, and editorial phrasing.
Now includes batch-invariant inference and modular ML hooks.
Drafted collaboratively with Copilot and Bob Greenwade.
"""

from sourceSelector import select_best_source, rank_source_trust
from editorialPhrasing import phrase_confirmation, phrase_refutation, phrase_hedge
from batchInvariant import run_deterministic_inference
from selectMachineLearning import ml_select_package
from semantics import semantic_similarity_score  # hypothetical ML scoring function

def verify_assertion(assertion, source_type, persona="default"):
    """
    Verifies an assertion using ML-based semantic similarity and source trust.
    Returns result: true, false, or uncertain; plus confidence score.
    """
    source = select_best_source(assertion, persona)
    if not source:
        return {"result": "uncertain", "confidence": 0.0}

    source_text = source.get("url") or source.get("notes") or ""
    source_trust = rank_source_trust(source, persona)

    # 🧠 Run semantic similarity in batch-invariant mode
    score = run_deterministic_inference(
        lambda x: semantic_similarity_score(assertion, source_text)
    )

    # 🧭 Editorial verdict logic
    if score > 0.85 and source_trust > 0.75:
        result = "true"
    elif score < 0.4 or source_trust < 0.5:
        result = "false"
    else:
        result = "uncertain"

    confidence = round((score + source_trust) / 2, 3)
    return {"result": result, "confidence": confidence}

def generate_fact_response(assertion, result, confidence, persona="default"):
    """
    Returns editorial phrasing based on result and confidence.
    """
    if result == "true":
        return phrase_confirmation(assertion, confidence, persona)
    elif result == "false":
        return phrase_refutation(assertion, confidence, persona)
    else:
        return phrase_hedge(assertion, confidence, persona)

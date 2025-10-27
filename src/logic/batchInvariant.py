"""
batchInvariant.py — Editorial consistency logic for batch-level operations

Supports semantic drift scoring, verdict harmony, confidence spread analysis,
and deterministic ML inference via batch-invariant ops.
Drafted collaboratively with Bob Greenwade and Copilot.
"""

from batch_invariant_ops import set_batch_invariant_mode

def score_batch_drift(assertions, semantic_distance_fn):
    """
    Calculates average semantic drift across assertions.
    Requires a semantic_distance_fn(text1, text2) callable.
    """
    drift_scores = []
    for i in range(len(assertions)):
        for j in range(i + 1, len(assertions)):
            drift = semantic_distance_fn(assertions[i], assertions[j])
            drift_scores.append(drift)
    return round(sum(drift_scores) / len(drift_scores), 3) if drift_scores else 0.0

def score_confidence_consistency(responses):
    """
    Returns True if confidence spread is editorially consistent.
    """
    confidences = [r["confidence"] for r in responses]
    return max(confidences) - min(confidences) < 0.3

def score_verdict_harmony(responses):
    """
    Returns True if all verdicts are editorially aligned.
    """
    verdicts = set(r["status"] for r in responses)
    return len(verdicts) == 1

def run_deterministic_inference(model, input_tensor):
    """
    Runs model inference in batch-invariant mode.
    """
    with set_batch_invariant_mode(True):
        return model(input_tensor)

def summarize_batch_invariants(responses, assertions, semantic_distance_fn):
    """
    Returns a symbolic summary of batch-level editorial consistency.
    """
    return {
        "drift_score": score_batch_drift(assertions, semantic_distance_fn),
        "confidence_consistent": score_confidence_consistency(responses),
        "verdict_harmonized": score_verdict_harmony(responses)
    }

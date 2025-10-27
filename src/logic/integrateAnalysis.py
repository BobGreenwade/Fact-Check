"""
integrateAnalysis.py — Synthesizes multimodal analysis for editorial validation

Combines text, audio, image, and document signals to assess truth, tone, and trust.
Supports semantic drift scoring, tone alignment, source corroboration, and editorial phrasing.
Drafted collaboratively with Copilot and Bob Greenwade.
"""

from semantics import detect_emotional_tone, estimate_confidence, detect_euphemism
from checkLogic import evaluate_logic
from editorialPhrasing import phrase_by_score
from topicClassifier import classify_topic
from sourceSelector import select_best_source
from selectMachineLearning import select_best_package
from configEditor import get_config_value

def integrate_text_analysis(assertion, known_facts=None, persona="default"):
    """
    Runs full editorial analysis on a single assertion.
    Returns structured report with phrasing and metadata.
    """
    known_facts = known_facts or []
    logic = evaluate_logic(assertion, known_facts)
    topics = classify_topic(assertion)
    top_topic = max(topics, key=topics.get)
    source = select_best_source(top_topic, persona)
    tone = detect_emotional_tone(assertion)
    confidence = estimate_confidence(assertion)
    phrasing = phrase_by_score(assertion, 1.0 - len(logic["fallacies"]) * 0.2, confidence, persona)

    return {
        "assertion": assertion,
        "topics": topics,
        "source": source,
        "logic": logic,
        "tone": tone,
        "confidence": confidence,
        "phrasing": phrasing
    }

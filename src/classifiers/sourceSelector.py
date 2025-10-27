"""
sourceSelector.py — Selects best source type for fact-checking

Evaluates viability, routes to internal or external sources, and scores trust.
Supports persona-aware bias calibration and symbolic sync lineage.
Drafted collaboratively with Copilot and Bob Greenwade.
"""

from editors import registryEditor
from syncGlyphs import get_sync_lineage  # Optional: symbolic trust lineage

def get_sources_for_topic(topic):
    registry = registryEditor.load_registry()
    return registry.get(topic, [])

def evaluate_source_viability(assertion_type, topic):
    supported_topics = ["politics", "science", "history", "health", "technology", "finance"]
    return assertion_type == "factual" and topic in supported_topics

def select_source_type(topic, assertion):
    internal_topics = ["history", "science"]
    web_topics = ["politics", "finance", "technology", "health"]

    if topic in internal_topics:
        return "internal_memory"
    elif topic in web_topics:
        return "external_web"
    else:
        return "knowledge_base"

def rank_source_trust(source_metadata, persona="default"):
    reliability_map = {"high": 1.0, "medium": 0.7, "low": 0.4}
    bias_penalty = {
        "neutral": 0.0,
        "slightly progressive": -0.1,
        "conservative": -0.2
    }
    tone_bonus = {
        "clinical": 0.1,
        "academic": 0.1,
        "playful": 0.05
    }

    score = reliability_map.get(source_metadata.get("reliability"), 0.5)
    score += tone_bonus.get(source_metadata.get("tone"), 0.0)
    score += bias_penalty.get(source_metadata.get("bias"), 0.0)
    return max(0.0, min(score, 1.0))

def select_best_source(topic, persona="default"):
    sources = get_sources_for_topic(topic)
    scored = [(s, rank_source_trust(s, persona)) for s in sources]
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[0][0] if scored else None

def get_source_lineage(source_name):
    """
    Returns symbolic sync lineage for a given source.
    Optional: used for editorial audit or trust propagation.
    """
    return get_sync_lineage(source_name)

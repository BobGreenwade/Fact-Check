"""
sourceSelector.py — Selects best source type for fact-checking

Evaluates viability, routes to internal or external sources, and scores trust.
Drafted collaboratively with Copilot and Bob Greenwade.
"""

def evaluate_source_viability(assertion_type, topic):
    """
    Determines whether the assertion is checkable.
    Returns True if factual and topic is supported.
    """
    supported_topics = ["politics", "science", "history", "health", "technology", "finance"]
    return assertion_type == "factual" and topic in supported_topics

def select_source_type(topic, assertion):
    """
    Chooses best source type: internal memory, knowledge base, or external web.
    Placeholder logic; refine with registry metadata and editorial tone.
    """
    internal_topics = ["history", "science"]
    web_topics = ["politics", "finance", "technology", "health"]

    if topic in internal_topics:
        return "internal_memory"
    elif topic in web_topics:
        return "external_web"
    else:
        return "knowledge_base"

def rank_source_trust(source_metadata):
    """
    Scores source reliability and editorial tone compatibility.
    Placeholder logic; refine with registry metadata and ML scoring.
    """
    score = 0
    if source_metadata.get("reliability") == "high":
        score += 2
    if source_metadata.get("bias") in ["neutral", None]:
        score += 1
    if source_metadata.get("tone") in ["clinical", "academic"]:
        score += 1
    return score

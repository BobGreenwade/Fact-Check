"""
topicClassifier.py — Classifies assertions by topic/domain

Supports editorial routing, source selection, and tone-aware tagging.
Drafted collaboratively with Copilot and Bob Greenwade.
"""

def classify_topic(assertion):
    """
    Returns one or more topic tags for the given assertion.
    Placeholder logic; refine with ML or rule-based classifier.
    """
    keywords = {
        "politics": ["president", "election", "congress", "senator", "policy"],
        "science": ["gravity", "atom", "experiment", "physics", "biology"],
        "history": ["war", "treaty", "empire", "revolution", "historical"],
        "health": ["disease", "symptom", "treatment", "vaccine", "mental health"],
        "technology": ["AI", "software", "internet", "device", "algorithm"],
        "culture": ["movie", "music", "celebrity", "art", "fashion"],
        "finance": ["stock", "market", "inflation", "interest rate", "economy"]
    }

    lowered = assertion.lower()
    matched_topics = []
    for topic, terms in keywords.items():
        if any(term in lowered for term in terms):
            matched_topics.append(topic)

    return matched_topics if matched_topics else ["general"]

def route_to_source_cluster(topic):
    """
    Maps topic to source registry cluster.
    Placeholder logic; refine with registry metadata.
    """
    cluster_map = {
        "politics": "gov_sources",
        "science": "peer_reviewed",
        "history": "academic",
        "health": "medical",
        "technology": "tech_news",
        "culture": "media",
        "finance": "financial"
    }
    return cluster_map.get(topic, "general")

def flag_sensitive_topic(topic):
    """
    Flags topics that require editorial caution.
    """
    sensitive = ["politics", "health", "finance"]
    return topic in sensitive

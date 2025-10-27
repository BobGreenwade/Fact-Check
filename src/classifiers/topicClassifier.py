"""
topicClassifier.py — Classifies assertions by topic/domain

Uses topic_tree.json for dynamic classification, editorial routing, and sensitivity tagging.
Drafted collaboratively with Copilot and Bob Greenwade.
"""

import json
import os
from editors.configEditor import get_config_value

TOPIC_TREE_PATH = "topic_tree.json"

def classify_topic(assertion):
    tree = load_topic_tree()
    lowered = assertion.lower()
    topic_scores = {}
    threshold = get_config_value("TOPIC_MATCH_THRESHOLD", 0.2)

    for topic, metadata in tree.items():
        keywords = metadata.get("keywords", [])
        hits = sum(1 for term in keywords if term.lower() in lowered)
        if hits:
            score = round(min(1.0, hits / len(keywords)), 2)
            if score >= threshold:
                topic_scores[topic] = score

    return topic_scores if topic_scores else {"general": 0.1}

def load_topic_tree(path=TOPIC_TREE_PATH):
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def route_to_source_cluster(topic):
    """
    Maps topic to source registry cluster using topic tree metadata.
    """
    tree = load_topic_tree()
    return tree.get(topic, {}).get("source_cluster", "general")

def flag_sensitive_topic(topic):
    """
    Flags topics that require editorial caution.
    """
    tree = load_topic_tree()
    return tree.get(topic, {}).get("sensitive", False)

def get_primary_topic(assertion):
    scores = classify_topic(assertion)
    return max(scores, key=scores.get) if scores else "general"

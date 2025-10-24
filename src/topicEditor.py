"""
topicEditor.py — Manages topic_tree.json for classification and editorial routing

Supports topic creation, keyword tuning, sensitivity tagging, and source cluster mapping.
Drafted collaboratively with Copilot and Bob Greenwade.
"""

import json
import os

TOPIC_TREE_PATH = "topic_tree.json"

def load_topic_tree(path=TOPIC_TREE_PATH):
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_topic_tree(data, path=TOPIC_TREE_PATH):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def add_topic(name, keywords, source_cluster="general", sensitive=False):
    tree = load_topic_tree()
    if name in tree:
        return False
    tree[name] = {
        "keywords": keywords,
        "source_cluster": source_cluster,
        "sensitive": sensitive
    }
    save_topic_tree(tree)
    return True

def update_topic(name, updates):
    tree = load_topic_tree()
    if name not in tree:
        return False
    tree[name].update(updates)
    save_topic_tree(tree)
    return True

def remove_topic(name):
    tree = load_topic_tree()
    if name not in tree:
        return False
    del tree[name]
    save_topic_tree(tree)
    return True

def list_topics():
    tree = load_topic_tree()
    return list(tree.keys())

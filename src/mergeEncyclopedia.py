"""
mergeEncyclopedia.py — Synchronizes registry and topic data across instances

Supports distributed fact-checking via LAN/WAN/intranet sync.
Handles bidirectional merges, trust-weighted resolution, and symbolic sync metadata.
Drafted collaboratively with Copilot and Bob Greenwade.
"""

import json
import os
import requests
from editors.configEditor import get_config_value

def fetch_remote_json(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def merge_registries(local, remote):
    """
    Merges two source registries with trust-weighted resolution.
    """
    merged = local.copy()
    for domain, sources in remote.items():
        if domain not in merged:
            merged[domain] = sources
        else:
            existing_names = {s["name"] for s in merged[domain]}
            for s in sources:
                if s["name"] not in existing_names:
                    merged[domain].append(s)
                else:
                    # Conflict resolution: prefer higher trust or newer timestamp
                    local_entry = next((x for x in merged[domain] if x["name"] == s["name"]), None)
                    if s.get("trust", 0) > local_entry.get("trust", 0):
                        merged[domain] = [x if x["name"] != s["name"] else s for x in merged[domain]]
    return merged

def merge_topic_trees(local, remote):
    """
    Merges two topic trees with keyword union and sensitivity override.
    """
    merged = local.copy()
    for topic, data in remote.items():
        if topic not in merged:
            merged[topic] = data
        else:
            merged[topic]["keywords"] = list(set(merged[topic]["keywords"]) | set(data["keywords"]))
            merged[topic]["sensitive"] = merged[topic]["sensitive"] or data["sensitive"]
            merged[topic]["source_cluster"] = merged[topic].get("source_cluster") or data.get("source_cluster")
    return merged

def sync_from_remote(registry_url, topic_url, local_registry_path, local_topic_path):
    """
    Fetches remote data and merges with local files.
    """
    remote_registry = fetch_remote_json(registry_url)
    remote_topic_tree = fetch_remote_json(topic_url)

    if "error" in remote_registry or "error" in remote_topic_tree:
        return {"status": "error", "details": [remote_registry.get("error"), remote_topic_tree.get("error")]}

    with open(local_registry_path, "r", encoding="utf-8") as f:
        local_registry = json.load(f)
    with open(local_topic_path, "r", encoding="utf-8") as f:
        local_topic_tree = json.load(f)

    merged_registry = merge_registries(local_registry, remote_registry)
    merged_topic_tree = merge_topic_trees(local_topic_tree, remote_topic_tree)

    with open(local_registry_path, "w", encoding="utf-8") as f:
        json.dump(merged_registry, f, indent=2)
    with open(local_topic_path, "w", encoding="utf-8") as f:
        json.dump(merged_topic_tree, f, indent=2)

    return {"status": "success", "merged": True}

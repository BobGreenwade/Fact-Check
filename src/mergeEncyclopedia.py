"""
mergeEncyclopedia.py — Synchronizes registry and topic data across instances

Supports distributed fact-checking via LAN/WAN/intranet sync.
Handles bidirectional merges, trust-weighted resolution, and symbolic sync metadata.
Drafted collaboratively with Copilot and Bob Greenwade.
"""
"""
syncGlyphs.py — Symbolic glyphs and rituals for distributed editorial sync

Encodes sync events as glyphs, tracks symbolic metadata, and supports
editorial ceremonies for trust propagation, merge validation, and sync lineage.
Drafted collaboratively with Bob Greenwade and Copilot.
"""

import hashlib
import random
from datetime import datetime

# 🧬 Glyph Generation
def generate_sync_glyph(source_id, target_id, timestamp=None):
    """
    Generates a symbolic glyph for a sync event.
    Combines source, target, and timestamp into a hash-based glyph.
    """
    timestamp = timestamp or datetime.utcnow().isoformat()
    seed = f"{source_id}|{target_id}|{timestamp}"
    glyph = hashlib.sha256(seed.encode()).hexdigest()[:12]
    return {
        "glyph": glyph,
        "source": source_id,
        "target": target_id,
        "timestamp": timestamp
    }

# 🧭 Ritual Metadata
def describe_sync_ritual(glyph_obj):
    """
    Returns a symbolic description of the sync event.
    Used for audit logs, dashboards, or editorial ceremonies.
    """
    phrases = [
        "The glyph was cast beneath a mirrored moon.",
        "Trust flowed from source to target like ink through vellum.",
        "Editorial lineage was braided into the glyph’s core.",
        "This sync bore the mark of semantic convergence.",
        "A ritual of reconciliation was performed at {timestamp}."
    ]
    chosen = random.choice(phrases)
    return chosen.format(**glyph_obj)

# 📜 Glyph Registry (Placeholder)
glyph_registry = []

def register_sync_glyph(glyph_obj):
    """
    Stores glyph metadata in the local registry.
    """
    glyph_registry.append(glyph_obj)
    print(f"[GLYPH] Registered sync glyph: {glyph_obj['glyph']}")

def get_sync_lineage(target_id):
    """
    Returns all glyphs where the given target_id was the recipient.
    """
    return [g for g in glyph_registry if g["target"] == target_id]

def summarize_sync_history():
    """
    Returns a symbolic summary of all sync glyphs.
    """
    return {
        "total_syncs": len(glyph_registry),
        "unique_sources": list(set(g["source"] for g in glyph_registry)),
        "unique_targets": list(set(g["target"] for g in glyph_registry))
    }
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

"""
mergeEncyclopedia.py — Synchronizes registry and topic data across instances

Supports distributed fact-checking via LAN/WAN/intranet sync.
Drafted collaboratively with Copilot and Bob Greenwade.
"""

import json
import os
import requests

def fetch_remote_registry(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def merge_registries(local, remote):
    """
    Merges two source registries.
    Placeholder logic: naive merge with overwrite preference.
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
    return merged

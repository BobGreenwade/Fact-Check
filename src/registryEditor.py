"""
registryEditor.py — Manage trusted source registry for Fact-Check module

Allows manual or programmatic updates to the source registry, including tagging for reliability, bias, editorial tone, and domain relevance.
Drafted collaboratively with Copilot and Bob Greenwade.
"""

import json
import os

REGISTRY_PATH = "source_registry.json"

def load_registry(path=REGISTRY_PATH):
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_registry(data, path=REGISTRY_PATH):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def add_source(domain, name, url, reliability, bias=None, tone=None, notes=None):
    registry = load_registry()
    if domain not in registry:
        registry[domain] = []
    registry[domain].append({
        "name": name,
        "url": url,
        "reliability": reliability,
        "bias": bias,
        "tone": tone,
        "notes": notes
    })
    save_registry(registry)
    return True

def update_source(domain, name, updates):
    registry = load_registry()
    if domain not in registry:
        return False
    for source in registry[domain]:
        if source["name"] == name:
            source.update(updates)
            save_registry(registry)
            return True
    return False

def remove_source(domain, name):
    registry = load_registry()
    if domain not in registry:
        return False
    registry[domain] = [s for s in registry[domain] if s["name"] != name]
    save_registry(registry)
    return True

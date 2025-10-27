"""
configEditor.py — Manages runtime configuration for Fact-Check and editorial modules

Supports persona defaults, fallback behavior, ML routing, and editorial tone settings.
Drafted collaboratively with Copilot and Bob Greenwade.
"""

import json
import os

CONFIG_PATH = "config.json"

def load_config(path=CONFIG_PATH):
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_config(config, path=CONFIG_PATH):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)

def update_config(key, value):
    config = load_config()
    config[key] = value
    save_config(config)
    return True

def get_config_value(key, default=None):
    config = load_config()
    return config.get(key, default)

def reset_config():
    default_config = {
        "DEFAULT_PERSONA": "default",
        "LOCATION_FALLBACK": "ask",
        "TRANSCRIPT_CONTEXT_BUFFER_SIZE": 10,
        "ML_ROUTING_MODE": "score_based",
        "EDITORIAL_TONE": "neutral",
        "ENABLE_SABOTAGE_TAGGING": True,
        "ENABLE_EUPHEMISM_DETECTION": True,
        "TRUST_THRESHOLD": 0.75
    }
    save_config(default_config)
    return default_config

def describe_config():
    config = load_config()
    return {
        "persona": config.get("DEFAULT_PERSONA", "default"),
        "tone": config.get("EDITORIAL_TONE", "neutral"),
        "routing": config.get("ML_ROUTING_MODE", "score_based"),
        "sabotage": config.get("ENABLE_SABOTAGE_TAGGING", True),
        "euphemism": config.get("ENABLE_EUPHEMISM_DETECTION", True),
        "trust_threshold": config.get("TRUST_THRESHOLD", 0.75)
    }

def config_exists(path=CONFIG_PATH):
    return os.path.exists(path)
    

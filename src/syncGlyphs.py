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

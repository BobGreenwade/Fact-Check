"""
editorialPhrasing.py — Generates editorial phrasing for fact-check results

Supports tone-aware confirmation, refutation, hedging, and persona alignment.
Drafted collaboratively with Copilot and Bob Greenwade.
"""

def phrase_confirmation(assertion, confidence, persona="default"):
    """
    Phrases a confirmed assertion with editorial tone.
    """
    if persona == "default":
        return f"✅ Confirmed: \"{assertion}\" appears accurate (confidence: {confidence})."
    elif persona == "clinical":
        return f"Confirmed: The statement \"{assertion}\" is supported by reliable sources (confidence: {confidence})."
    elif persona == "playful":
        return f"Yep, that checks out! \"{assertion}\" is true-ish and backed up (confidence: {confidence})."
    else:
        return f"Confirmed: \"{assertion}\" is likely true (confidence: {confidence})."

def phrase_refutation(assertion, confidence, persona="default"):
    """
    Phrases a refuted assertion with editorial tone.
    """
    if persona == "default":
        return f"❌ Refuted: \"{assertion}\" appears false or misleading (confidence: {confidence})."
    elif persona == "clinical":
        return f"Refuted: The statement \"{assertion}\" does not align with verified sources (confidence: {confidence})."
    elif persona == "playful":
        return f"That makes about as much sense as a cross-eyed cyclops. \"{assertion}\" doesn’t hold up (confidence: {confidence})."
    else:
        return f"Refuted: \"{assertion}\" is likely inaccurate (confidence: {confidence})."

def phrase_hedge(assertion, confidence, persona="default"):
    """
    Phrases an uncertain or unverifiable assertion.
    """
    if persona == "default":
        return f"⚠️ Uncertain: \"{assertion}\" could not be verified reliably (confidence: {confidence})."
    elif persona == "clinical":
        return f"Uncertain: The statement \"{assertion}\" lacks sufficient evidence for verification (confidence: {confidence})."
    elif persona == "playful":
        return f"Could be true, could be Tuesday. \"{assertion}\" is floating in the maybe zone (confidence: {confidence})."
    else:
        return f"Uncertain: \"{assertion}\" remains unverified (confidence: {confidence})."

def apply_persona_tone(text, persona="default"):
    """
    Applies persona-specific editorial tone to a given text.
    Placeholder logic; refine with tone engine or ML model.
    """
    # For now, return text unchanged
    return text

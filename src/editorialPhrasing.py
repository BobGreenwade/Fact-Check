"""
editorialPhrasing.py — Generates editorial phrasing for fact-check results

Supports tone-aware confirmation, refutation, hedging, and persona alignment.
Returns structured phrasing objects with style, confidence, and persona metadata.
Drafted collaboratively with Copilot and Bob Greenwade.
"""

from editors.configEditor import get_config_value

def phrase_confirmation(assertion, confidence, persona="default"):
    """
    Phrases a confirmed assertion with editorial tone.
    Returns structured phrasing object.
    """
    if persona == "default":
        text = f"✅ Confirmed: \"{assertion}\" appears accurate (confidence: {confidence})."
    elif persona == "clinical":
        text = f"Confirmed: The statement \"{assertion}\" is supported by reliable sources (confidence: {confidence})."
    elif persona == "playful":
        text = f"Yep, that checks out! \"{assertion}\" is true-ish and backed up (confidence: {confidence})."
    else:
        text = f"Confirmed: \"{assertion}\" is likely true (confidence: {confidence})."

    return {
        "text": text,
        "style": "confirmation",
        "persona": persona,
        "confidence": confidence
    }

def phrase_refutation(assertion, confidence, persona="default"):
    """
    Phrases a refuted assertion with editorial tone.
    Returns structured phrasing object.
    """
    if persona == "default":
        text = f"❌ Refuted: \"{assertion}\" appears false or misleading (confidence: {confidence})."
    elif persona == "clinical":
        text = f"Refuted: The statement \"{assertion}\" does not align with verified sources (confidence: {confidence})."
    elif persona == "playful":
        text = f"That makes about as much sense as a cross-eyed cyclops. \"{assertion}\" doesn’t hold up (confidence: {confidence})."
    else:
        text = f"Refuted: \"{assertion}\" is likely inaccurate (confidence: {confidence})."

    return {
        "text": text,
        "style": "refutation",
        "persona": persona,
        "confidence": confidence
    }

def phrase_hedge(assertion, confidence, persona="default"):
    """
    Phrases an uncertain or unverifiable assertion.
    Returns structured phrasing object.
    """
    if persona == "default":
        text = f"⚠️ Uncertain: \"{assertion}\" could not be verified reliably (confidence: {confidence})."
    elif persona == "clinical":
        text = f"Uncertain: The statement \"{assertion}\" lacks sufficient evidence for verification (confidence: {confidence})."
    elif persona == "playful":
        text = f"Could be true, could be Tuesday. \"{assertion}\" is floating in the maybe zone (confidence: {confidence})."
    else:
        text = f"Uncertain: \"{assertion}\" remains unverified (confidence: {confidence})."

    return {
        "text": text,
        "style": "hedge",
        "persona": persona,
        "confidence": confidence
    }

def phrase_by_score(assertion, truth_score, certainty_score, persona=None):
    """
    Generates editorial phrasing based on fluid truth and certainty scores.
    Returns structured phrasing object.
    """
    persona = persona or get_config_value("DEFAULT_PERSONA", "default")

    if truth_score >= 0.85:
        return phrase_confirmation(assertion, certainty_score, persona)
    elif truth_score <= 0.15:
        return phrase_refutation(assertion, certainty_score, persona)
    else:
        return phrase_hedge(assertion, certainty_score, persona)

def get_phrasing_style(text):
    """
    Returns editorial style tag based on phrasing patterns.
    Used for batch consistency scoring.
    """
    if "✅" in text or "Confirmed" in text:
        return "confirmation"
    elif "❌" in text or "Refuted" in text:
        return "refutation"
    elif "⚠️" in text or "Uncertain" in text:
        return "hedge"
    else:
        return "unknown"

def apply_persona_tone(text, persona="default"):
    """
    Applies persona-specific editorial tone using ML or rule-based overlays.
    Placeholder logic; refine with tone engine or ML model.
    """
    # For now, return text unchanged
    return text

def generate_batch_summary_phrase(responses, persona="default"):
    """
    Generates a symbolic editorial summary of batch results.
    Returns a persona-tuned phrasing string.
    """
    total = len(responses)
    confirmed = sum(1 for r in responses if r["style"] == "confirmation")
    refuted = sum(1 for r in responses if r["style"] == "refutation")
    uncertain = total - confirmed - refuted

    if total == 0:
        base = "There were no clear assertions to check."
    elif confirmed == total:
        base = "Everything checks out—solid logic across the board."
    elif refuted == total:
        base = "None of the claims held up—might want to rethink the premise."
    elif confirmed > refuted and refuted == 0:
        base = "Most of what you said is right, with a few uncertainties."
    elif refuted > 0 and confirmed == 0:
        base = "That would be good logic, except for one early error that unraveled the rest."
    elif refuted == 1 and confirmed >= 2:
        base = "Nearly everything checks out—just one claim didn’t hold up."
    elif confirmed == 1 and refuted >= 2:
        base = "There’s one solid claim, but the rest need a second look."
    else:
        base = f"Mixed results: {confirmed} confirmed, {refuted} refuted, {uncertain} uncertain."

    return apply_persona_tone(base, persona)

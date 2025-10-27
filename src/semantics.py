"""
semantics.py — Editorial semantic matching and rhythm-aware analysis

Provides synonym expansion, word-form normalization, semantic matching,
phrase structure detection, euphemism flagging, and conceptual drift scoring.
Supports emotional tone detection, confidence tagging, and reality mode classification.
Drafted collaboratively with Bob Greenwade and Copilot.
"""

import re
import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from learning import run_learning

lemmatizer = WordNetLemmatizer()

# 🔁 Core Normalization and Matching
def normalize_word(word):
    return lemmatizer.lemmatize(word.lower())

def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name().lower())
    return synonyms

def match_semantic(word, target_list):
    normalized = normalize_word(word)
    synonyms = get_synonyms(normalized)
    expanded = synonyms.union({normalized})
    return any(t in expanded for t in target_list)

def match_phrase(text, phrase_list):
    lowered = text.lower()
    return any(phrase.lower() in lowered for phrase in phrase_list)

def match_wordlist(text, wordlist):
    tokens = text.lower().split()
    for token in tokens:
        if match_semantic(token, wordlist):
            return True
    return False

# 🧠 Rhythm and Structure Detection
def match_phrase_structure(text):
    clauses = re.split(r"[.,;!?]", text)
    rhythm = "short" if all(len(c.strip().split()) <= 6 for c in clauses) else "mixed"
    punctuation = [p for p in text if p in ".!?"]
    return {
        "clause_count": len(clauses),
        "rhythm": rhythm,
        "punctuation": punctuation
    }

# 🧭 Euphemism Detection
def detect_euphemism(text):
    softeners = [
        "passed away", "let go", "downsized", "special", "unique",
        "challenging", "differently abled", "nontraditional", "alternative"
    ]
    match = match_phrase(text, softeners)

    try:
        ml_result = run_learning("euphemism_detection", {"text": text})
        match = match or ml_result.get("output", {}).get("euphemism_detected", False)
    except Exception:
        pass

    return match

# 🔁 Semantic Drift and Distance
def semantic_distance(text1, text2):
    try:
        ml_result = run_learning("semantic_distance", {
            "text1": text1,
            "text2": text2
        })
        return round(ml_result.get("output", {}).get("distance", 0.5), 2)
    except Exception:
        return 0.5

# 🧠 Reality Mode Classification
def classify_reality_mode(text):
    try:
        ml_result = run_learning("reality_mode", {"text": text})
        return ml_result.get("output", {}).get("mode", "literal")
    except Exception:
        return "literal"

# 🎭 Emotional Tone Detection
def detect_emotional_tone(text):
    try:
        ml_result = run_learning("emotional_tone", {"text": text})
        return ml_result.get("output", {"tone": "neutral", "intensity": 0.0})
    except Exception:
        return {"tone": "neutral", "intensity": 0.0}

# 📊 Confidence Estimation
def estimate_confidence(text):
    try:
        ml_result = run_learning("confidence_estimation", {"text": text})
        return round(ml_result.get("output", {}).get("confidence", 0.5), 2)
    except Exception:
        return 0.5

"""
selectMachineLearning.py — Detects and selects available ML packages

Supports modular fallback and package-specific routing.
Drafted collaboratively with Copilot and Bob Greenwade.
"""

import importlib

ML_PACKAGES = {
    "spacy": "spaCy NLP",
    "transformers": "Hugging Face Transformers",
    "sklearn": "Scikit-learn",
    "textblob": "TextBlob",
    "nltk": "NLTK",
    "openai": "OpenAI API",
    "cohere": "Cohere API"
}

def check_installed_packages():
    available = {}
    for pkg in ML_PACKAGES:
        try:
            importlib.import_module(pkg)
            available[pkg] = ML_PACKAGES[pkg]
        except ImportError:
            continue
    return available

def select_best_package(task="classification"):
    available = check_installed_packages()
    if task == "classification":
        for preferred in ["transformers", "spacy", "sklearn"]:
            if preferred in available:
                return preferred
    elif task == "parsing":
        for preferred in ["spacy", "nltk"]:
            if preferred in available:
                return preferred
    elif task == "tone":
        for preferred in ["textblob", "transformers"]:
            if preferred in available:
                return preferred
    return None

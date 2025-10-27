"""
selectMachineLearning.py — Detects and selects available ML packages

Supports modular fallback, score-based selection, and future ML routing.
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

def score_package_for_task(pkg, task):
    """
    Assigns a score to each package for a given task.
    Placeholder logic; refine with ML or usage analytics.
    """
    score_map = {
        "classification": {
            "transformers": 0.95,
            "spacy": 0.85,
            "sklearn": 0.80
        },
        "parsing": {
            "spacy": 0.90,
            "nltk": 0.75
        },
        "tone": {
            "textblob": 0.80,
            "transformers": 0.85
        }
    }
    return score_map.get(task, {}).get(pkg, 0.0)

def select_best_package(task="classification"):
    available = check_installed_packages()
    scored = [(pkg, score_package_for_task(pkg, task)) for pkg in available]
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[0][0] if scored else None

def ml_select_package(task, context_features=None):
    """
    Placeholder for ML-based package selection.
    Could use decision trees, embeddings, or reinforcement learning.
    """
    # For now, fallback to score-based selection
    return select_best_package(task)

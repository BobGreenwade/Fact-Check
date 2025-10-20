# 🧠 Fact-Check Module

Modular validator for textual assertions. Accepts a stream of text, extracts claims, classifies topics, selects sources, and evaluates truthfulness with editorial nuance.

## 📦 Submodules

| Module | Role |
|--------|------|
| `segment_text.py` | Breaks input into assertion-ready chunks |
| `topic_classifier.py` | Tags each segment with its domain |
| `source_selector.py` | Chooses best source(s) for validation |
| `check_fact.py` | Verifies claim against selected source |
| `editorial_phrasing.py` | Crafts output with editorial nuance |
| `batch_check.py` | Handles multi-assertion streams |
| `registry.py` | Stores known facts and sources |
| `registryEditor.py` | Planned utility for registry management |
| `checkLogic.py` | Detects contradictions, fallacies, and rhetorical misdirection |

## 🔧 ML Integration

Supports modular fallback via `selectMachineLearning.py`. Initial candidates include:
- `spaCy`, `transformers`, `scikit-learn`, `nltk`, `textblob`, `openai`, `cohere`

## 🧩 Editorial Philosophy

- Validate with nuance, editorialize with rhythm, and license with conscience.
- MIT license for development; MPL or Apache for deployment once registry is ready.
- Supports persona-aware phrasing, emotional tone mapping, and contradiction tagging.

## 🛠️ Status

All core modules scaffolded. ML hooks and editorial phrasing logic in progress. Ready for collaborative refinement and integration.

---

And remember: Today is the tomorrow that you worried about yesterday...

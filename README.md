# 🧠 Fact-Check Module

Modular validator for textual assertions. Accepts a stream of text, extracts claims, classifies topics, selects sources, and evaluates truthfulness with editorial nuance.

## 🎯 Editorial Philosophy

- Supports persona-aware phrasing, tone modulation, and rhythm-aware editorial output.
- Prioritizes verifiable facts over opinions or ideology.
- Designed for modular clarity, editorial integrity, and future ML integration.

## 📦 Submodules (Alphabetical)

| Module | Role |
|--------|------|
| `batchCheck.py` | Processes multi-assertion input and returns structured results |
| `checkFact.py` | Verifies individual assertions and generates editorial phrasing |
| `checkLogic.py` | Detects contradictions, fallacies, and rhetorical misdirection |
| `editorialPhrasing.py` | Crafts tone-aware phrasing for confirmation, refutation, and hedging |
| `location.py` | Resolves user location for editorial routing and fallback logic |
| `paraphrase.py` | Persona-aware paraphrasing using LLM prompt construction |
| `registryEditor.py` | Manages source registry metadata including reliability and bias |
| `segmentText.py` | Splits text into sentences and extracts assertions |
| `selectMachineLearning.py` | Detects available ML packages and routes tasks accordingly |
| `sourceSelector.py` | Chooses best source type and scores trustworthiness |
| `topicClassifier.py` | Tags assertions with one or more dynamic topic domains |

## 🔮 Future Enhancements

- Integrate logical fallacy taxonomy from [logicalfallacies.org](https://logicalfallacies.org) into `checkLogic.py`
- Enable adaptive learning to adjust source reliability based on editorial outcomes
- Connect with image, video, audio, and document analysis modules to detect falsification

## 📜 License

- MIT License for development and prototyping
- Planned transition to MPL or Apache for deployment once source registry is validated

---

And remember: Take good care of your brain. You're going to need it later.

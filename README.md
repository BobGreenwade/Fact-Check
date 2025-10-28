# 🧠 Fact-Check Module

Modular validator for textual assertions. Accepts a stream of text, extracts claims, classifies topics, selects sources, and evaluates truthfulness with editorial nuance.

## 🎯 Editorial Philosophy

- Supports persona-aware phrasing, tone modulation, and rhythm-aware editorial output  
- Prioritizes verifiable facts over opinions or ideology  
- Designed for modular clarity, editorial integrity, and future ML integration  

## 📦 Submodules by Directory

### `src/` - Primary files
| Module | Role |
|--------|------| 
| `editorialPhrasing.py` | Crafts tone-aware phrasing for confirmation, refutation, and hedging  
| `location.py` | Resolves user location for editorial routing and fallback logic  
| `mergeEncyclopedia.py` | Synchronizes source and topic data across distributed instances  
| `syncGlyphs.py` | Synchronizes glyphs across databases
| `transcript.py` | Captures context-aware conversation logs with escalation triggers  

### `src/classifiers/` — Topic, Source, and ML Routing  
| Module | Role |  
|--------|------|  
| `selectMachineLearning.py` | Detects available ML packages and routes tasks accordingly  
| `sourceSelector.py` | Chooses best source type and scores trustworthiness  
| `topicClassifier.py` | Tags assertions with one or more dynamic topic domains  

### `src/data/` - JSON Configuration
| File | Role |
|------|------|
| `source_registry.json` | Trusted sources with reliability, bias, tone, and notes  
| `topic_tree.json` | Topic definitions, keywords, source clusters, and sensitivity flags  

### `src/editors/` — Editorial Tone and Configuration  
| Module | Role |  
|--------|------|  
| `configEditor.py` | Manages runtime configuration and editorial toggles  
| `registryEditor.py` | Manages source registry metadata including reliability and bias  
| `topicEditor.py` | Edits topic tree metadata, keywords, and sensitivity flags  

### `src/logic/` — Core Editorial and Verification Logic  
| Module | Role |  
|--------|------|  
| `batchCheck.py` | Processes multi-assertion input and returns structured results  
| `batchInvariant.py` | Helps maintain logical consistency 
| `checkFact.py` | Verifies individual assertions and generates editorial phrasing  
| `checkLogic.py` | Detects contradictions, fallacies, and rhetorical misdirection  
| `integrateAnalysis.py` | Synthesizes multimodal analysis for editorial verdicts  
| `segmentText.py` | Splits text into sentences and extracts assertions  

## 🗃️ JSON Configuration

- `source_registry.json` — Trusted sources with reliability, bias, tone, and notes  
- `topic_tree.json` — Topic definitions, keywords, source clusters, and sensitivity flags  

## 🔮 Future Enhancements

- Integrate logical fallacy taxonomy from [logicalfallacies.org](https://logicalfallacies.org) into `checkLogic.py`  
- Enable adaptive learning to adjust source reliability based on editorial outcomes  
- Connect with image, video, audio, and document analysis modules to detect falsification and forgery   

---

**And remember: If at first you don't succeed, rely on your fallback logic.**

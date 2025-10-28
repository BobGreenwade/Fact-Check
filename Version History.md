# Version History — Fact-Check Editorial Suite  
Curated by Bob Greenwade and Copilot  
Last updated: 2025-10-23

---

## v0.0.3 — Frame  
**Date:** 2025-10-27  
**Status:** Editorially consistent, batch-aware, and ready for multimodal synthesis

### 🔧 Modules Enhanced or Added
- `batchCheck.py` — Returns structured responses and batch-level editorial summary
- `checkFact.py` — Refactored for ML-based verification and batch-invariant inference
- `checkLogic.py` — Expanded with sabotage scoring and ML hooks
- `segmentText.py` — Assertion tagging and compound expansion logic refined
- `editorialPhrasing.py` — Persona-aware phrasing and batch summary generation
- `batchInvariant.py` — New module for semantic drift scoring, verdict harmony, and deterministic ML inference

### 🧠 Editorial Enhancements
- Batch-level consistency scoring and symbolic summary phrasing
- ML-ready assertion typing and semantic similarity scaffolding
- Deterministic inference via `batch_invariant_ops`
- Persona-aware phrasing for confirmation, refutation, and hedging
- Compound subject expansion and sabotage detection

### 🔮 Future Integration Hooks
- Image, video, and media analysis modules for multimodal synthesis
- Dashboard modules (`glyphAudit.py`, `trustDashboard.py`) for editorial visualization

---

## v0.0.2 — Foundation  
**Date:** 2025-10-23  
**Status:** Stable editorial core, ready for ML integration and modular expansion

### 🔧 New Modules Added
- `configEditor.py` — Runtime configuration manager
- `integrateAnalysis.py` — Multimodal synthesis and editorial verdicts
- `topicEditor.py` — Topic tree management and keyword tuning
- `mergeEncyclopedia.py` — Distributed sync across LAN/WAN/intranet

### 🗃️ JSON Files Activated
- `source_registry.json` — Trusted sources with reliability, bias, tone
- `topic_tree.json` — Topic definitions, keywords, clusters, sensitivity

### 🧹 Deprecated Modules
- `paraphrase.py` — Replaced by standalone semantic scoring tools (planned `semanticTools.py`)

### 🧠 Editorial Enhancements
- Sabotage tagging, euphemism detection, persona-aware phrasing
- Topic sensitivity flags and source cluster routing
- Configurable ML routing and fallback logic

---

## v0.0.1 — Scaffolding  
**Date:** 2025-10-22  
**Status:** Initial module layout and editorial intent

### 🔧 Core Modules Introduced
- `checkFact.py`, `checkLogic.py`, `segmentText.py`
- `selectMachineLearning.py`, `sourceSelector.py`, `topicClassifier.py`
- `registryEditor.py`, `transcript.py`, `semantics.py`

### 🗃️ Initial JSON Concepts
- `source_registry.json` (planned)
- `topic_tree.json` (planned)

### 🧠 Editorial Goals
- Rhythm-aware phrasing
- Fallacy detection
- Source trust scoring
- Modular ML routing

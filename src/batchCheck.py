"""
batchCheck.py — Processes multiple assertions in sequence

Runs full fact-check pipeline on multi-claim input and returns structured results.
Drafted collaboratively with Copilot and Bob Greenwade.
"""

from segmentText import split_into_sentences, extract_assertions, tag_assertion_type
from topicClassifier import classify_topic, route_to_source_cluster
from sourceSelector import evaluate_source_viability, select_source_type
from checkFact import verify_assertion, generate_fact_response
from editorialPhrasing import phrase_confirmation, phrase_refutation, phrase_hedge

def process_batch(text, persona="default"):
    """
    Processes a block of text through the full fact-check pipeline.
    Returns list of structured editorial responses.
    """
    responses = []
    sentences = split_into_sentences(text)
    for sentence_index, sentence in enumerate(sentences):
        assertions = extract_assertions(sentence)
        for assertion in assertions:
            assertion_type = tag_assertion_type(assertion)
            topic = classify_topic(assertion)
            if not evaluate_source_viability(assertion_type, topic):
                phrasing = phrase_hedge(assertion, confidence=0.0, persona=persona)
                result = "uncertain"
                confidence = 0.0
                source_type = "none"
            else:
                source_type = select_source_type(topic, assertion)
                verification = verify_assertion(assertion, source_type)
                result = verification["result"]
                confidence = verification["confidence"]
                if result == "true":
                    phrasing = phrase_confirmation(assertion, confidence, persona)
                elif result == "false":
                    phrasing = phrase_refutation(assertion, confidence, persona)
                else:
                    phrasing = phrase_hedge(assertion, confidence, persona)
            responses.append({
                "sentence_index": sentence_index,
                "assertion": assertion,
                "status": result if result in ["true", "false"] else "uncertain",
                "confidence": round(confidence, 2),
                "main_source": source_type,
                "phrasing": phrasing
            })
    return responses

def summarize_results(responses):
    """
    Summarizes batch results into structured assertion sets.
    Each set includes: assertion, status, certainty, and main source.
    """
    summary = []
    for r in responses:
        status_map = {
            "true": "confirmed",
            "false": "refuted",
            "uncertain": "uncertain"
        }
        summary.append({
            "assertion": r.get("assertion", ""),
            "status": status_map.get(r.get("status", "uncertain")),
            "certainty": r.get("confidence", 0.0),
            "main_source": r.get("main_source", "none")
        })
    return summary

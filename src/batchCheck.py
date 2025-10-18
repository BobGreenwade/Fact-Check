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
    Returns list of editorialized responses.
    """
    responses = []
    sentences = split_into_sentences(text)
    for sentence in sentences:
        assertions = extract_assertions(sentence)
        for assertion in assertions:
            assertion_type = tag_assertion_type(assertion)
            topic = classify_topic(assertion)
            if not evaluate_source_viability(assertion_type, topic):
                phrasing = phrase_hedge(assertion, confidence=0.0, persona=persona)
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
            responses.append(phrasing)
    return responses

def summarize_results(responses):
    """
    Summarizes batch results into a structured report.
    Placeholder logic; refine with editorial tags and tone metadata.
    """
    summary = {
        "total": len(responses),
        "confirmed": sum("✅" in r for r in responses),
        "refuted": sum("❌" in r for r in responses),
        "uncertain": sum("⚠️" in r for r in responses),
        "phrased": responses
    }
    return summary

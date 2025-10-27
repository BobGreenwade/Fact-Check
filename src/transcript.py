"""
transcript.py — Context-aware transcript logging for DLI

Captures conversation history when triggered, with pre-escalation context.
Drafted collaboratively with Copilot.
"""

import os
import json
from datetime import datetime
from editors.configEditor import get_config_value

BUFFER_SIZE = get_config_value("TRANSCRIPT_CONTEXT_BUFFER_SIZE", 10)

# Load config
def load_config(path="config.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

CONFIG = load_config()
BUFFER_SIZE = CONFIG.get("TRANSCRIPT_CONTEXT_BUFFER_SIZE", 10)

# Buffers and logs
context_buffer = []
transcript_log = []
transcript_active = False
transcript_trigger = None

def update_context_buffer(turn):
    context_buffer.append(turn)
    if len(context_buffer) > BUFFER_SIZE:
        context_buffer.pop(0)

def start_transcript(trigger_type="automatic"):
    global transcript_active, transcript_trigger
    if not transcript_active:
        transcript_log.extend(context_buffer)
        transcript_trigger = trigger_type
        transcript_active = True
        print(f"[TRANSCRIPT] Started via {trigger_type}")

def append_to_transcript(speaker, text, metadata=None):
    if transcript_active:
        entry = {
            "timestamp": datetime.now().isoformat(),
            "speaker": speaker,
            "text": text,
            "metadata": metadata or {}
        }
        transcript_log.append(entry)
        
def save_transcript(username="User"):
    if not transcript_active:
        print("[TRANSCRIPT] No active transcript to save.")
        return None

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"{username}_{timestamp}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        # 🧠 Transcript metadata block
        f.write(f"Transcript triggered by: {transcript_trigger}\n")
        f.write(f"Timestamp: {timestamp}\n")
        f.write(f"Buffer size: {BUFFER_SIZE}\n\n")

        # 🗒️ Transcript entries
        for entry in transcript_log:
            line = f"{entry['speaker']}: {entry['text']}"
            if entry["metadata"]:
                line += f" [{entry['metadata']}]"
            f.write(line + "\n")

    print(f"[TRANSCRIPT] Saved to {filename}")
    log_transcript_creation(filename, transcript_trigger)
    reset_transcript()
    return filename

def reset_transcript():
    global transcript_log, transcript_active, transcript_trigger
    transcript_log = []
    transcript_active = False
    transcript_trigger = None

def log_transcript_creation(filename, trigger):
    """
    Logs transcript creation for audit or learning.
    Placeholder for future registry or dashboard.
    """
    print(f"[TRANSCRIPT] Logged creation: {filename} via {trigger}")

def get_transcript_summary():
    return {
        "trigger": transcript_trigger,
        "length": len(transcript_log),
        "speakers": list(set(entry["speaker"] for entry in transcript_log))
    }

"""
Core AI Framework Proof-of-Concept Demo
Licensed under CC BY-NC 4.0
https://creativecommons.org/licenses/by-nc/4.0/

This demo showcases the Core cognitive loop:
User → Plan → LLM → Reflection → Memory Update → Persona

This file intentionally uses a reference Core implementation
to avoid exposing proprietary architecture.
"""

import sys

# Ensure the Python version matches the README requirement
if sys.version_info < (3, 10):
    raise RuntimeError("This demo requires Python 3.10 or higher.")

import time
import json
from datetime import datetime
from prettytable import PrettyTable
from core_demo_reference import Core  # Safe public reference Core


# ---------- Utility Logging ----------

def log_memory(event):
    """Persist episodic/semantic memory traces for auditability."""
    with open("core_memory_log.jsonl", "a") as f:
        f.write(json.dumps(event) + "\n")


# ---------- Demo Simulation ----------

def simulate_demo():
    core = Core()

    # Explain the architecture at the start
    print("\n=== Core AI Framework Demo ===")
    print(core.explain_architecture())

    demo_commands = [
        "Plan my schedule for today",
        "Reflect on my last decision",
        "Summarize recent interactions",
        "Suggest a creative solution for my project"
    ]

    table = PrettyTable()
    table.field_names = ["User Command", "Plan", "LLM Output", "Reflection Summary"]

    for cmd in demo_commands:
        print(f"\n[USER] {cmd}")
        time.sleep(0.4)

        # Core cognitive cycle
        result = core.run_cycle(cmd)

        plan = result.get("plan", "No plan generated")
        llm_resp = result.get("llm_response", "No LLM output")
        reflection = result.get("reflection", "No reflection stored")

        # Store structured memory trace
        memory_event = {
            "timestamp": datetime.utcnow().isoformat(),
            "command": cmd,
            "plan": plan,
            "llm_response": llm_resp,
            "reflection": reflection
        }
        log_memory(memory_event)

        # Display cognition trace
        print(f"[CORE] Plan Generated:\n  {plan}")
        time.sleep(0.2)

        print(f"[CORE] LLM Response:\n  {llm_resp}")
        time.sleep(0.2)

        print(f"[CORE] Reflection Stored:\n  {reflection}")
        time.sleep(0.2)

        print("[CORE] Episodic & semantic memory updated.\n")

        # Add to summary table
        table.add_row([cmd, plan, llm_resp, reflection])

    print("\n=== Demo Summary Table ===")
    print(table)
    print("\nMemory log saved to: core_memory_log.jsonl")


# ---------- Entry Point ----------

if __name__ == "__main__":
    simulate_demo()

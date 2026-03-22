from agent.analyzer import analyze_log
from actions.k8s_actions import restart_deployment
import ollama
import os

def llm(prompt):
    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]


def decide_and_act(log, analysis):
    log_lower = log.lower()
    analysis_lower = analysis.lower()

    if "oomkilled" in log_lower or "memory" in analysis_lower:
        print("⚡ AI Decision: Memory issue detected")
        restart_deployment("user-service")

    elif "crashloopbackoff" in log_lower or "crash" in analysis_lower:
        print("⚡ AI Decision: Crash detected")
        restart_deployment("payment-service")

    elif "database" in analysis_lower:
        print("⚡ AI Decision: Database issue detected")

    else:
        print("✅ No action needed")


def run():
    print("🚀 AI DevOps Agent Running...\n")

    log_file = "logs/sample_logs.txt"

    # ✅ Check if file exists
    if not os.path.exists(log_file):
        print("❌ Log file not found")
        return

    with open(log_file) as f:
        logs = f.readlines()

    for log in logs:

        # ✅ Filter only useful logs (real SRE behavior)
        if "ERROR" not in log and "WARNING" not in log:
            continue

        print("\n==============================")
        print(f"📌 Log: {log.strip()}")

        try:
            analysis = analyze_log(llm, log)
        except Exception as e:
            print("❌ AI Analysis failed:", e)
            continue

        print("\n🤖 AI Analysis:\n", analysis)

        print("\n⚡ Action:")
        decide_and_act(log, analysis)

        print("==============================")


if __name__ == "__main__":
    run()
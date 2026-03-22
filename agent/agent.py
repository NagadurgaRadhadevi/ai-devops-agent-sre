from agent.analyzer import analyze_log
from actions.k8s_actions import restart_deployment
import ollama

def llm(prompt):
    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]

def decide_and_act(log, analysis):
    analysis_lower = analysis.lower()
    log_lower = log.lower()

    if "oom" in log_lower or "memory" in analysis_lower:
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

    with open("logs/sample_logs.txt") as f:
        logs = f.readlines()

    for log in logs:
        print(f"\n📌 Log: {log.strip()}")

        analysis = analyze_log(llm, log)

        print("🤖 AI Analysis:\n", analysis)

        decide_and_act(log, analysis)

if __name__ == "__main__":
    run()
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
    if "OOMKilled" in log or "memory" in log:
        print("⚡ Action: Restarting due to memory issue")
        restart_deployment("user-service")

    elif "CrashLoopBackOff" in log:
        print("⚡ Action: Restarting crashing service")
        restart_deployment("payment-service")

    elif "database" in log.lower():
        print("⚡ Action: Investigate DB issue")

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
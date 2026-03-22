import ollama

def analyze_log(log):
    prompt = f"""
You are an expert Site Reliability Engineer (SRE).

Analyze the following log and provide:
1. Root Cause
2. Impact
3. Suggested Fix

Log:
{log}
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]


def run():
    with open("logs/sample_logs.txt") as f:
        log = f.read()

    result = analyze_log(log)

    print("\n=== AI Analysis ===\n")
    print(result)


if __name__ == "__main__":
    run()
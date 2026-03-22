def analyze_log(llm, log):
    prompt = f"""
You are an expert Site Reliability Engineer.

Analyze the log and give:
1. Root Cause
2. Impact
3. Fix

Log:
{log}
"""
    return llm(prompt)
def analyze_log(llm, log):
    prompt = f"""
You are an expert SRE.

Analyze:
1. Root Cause
2. Impact
3. Fix

Log:
{log}
"""
    return llm(prompt)
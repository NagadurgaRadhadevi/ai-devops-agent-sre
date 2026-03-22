def analyze_log(agent, log):
    prompt = f"""
You are an expert Site Reliability Engineer (SRE).

Analyze the following log and provide:
1. Root Cause
2. Impact
3. Suggested Fix

Log:
{log}
"""
    return agent(prompt)
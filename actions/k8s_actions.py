import os

def restart_deployment(service):
    print(f"🚀 Restarting deployment: {service}")
    os.system(f"kubectl rollout restart deployment {service}")
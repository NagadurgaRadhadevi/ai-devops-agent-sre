import os

def restart_deployment(deployment_name):
    print(f"Restarting deployment: {deployment_name}")
    os.system(f"kubectl rollout restart deployment {deployment_name}")
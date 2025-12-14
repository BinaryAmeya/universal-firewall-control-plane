import yaml

def load_policies():
    with open("policy/firewall_policies.yaml") as f:
        return yaml.safe_load(f)["policies"]

def match_policy(risk_score):
    for policy in load_policies():
        threshold = int(policy["condition"]["risk_score"].replace(">", ""))
        if risk_score > threshold:
            return policy
    return None

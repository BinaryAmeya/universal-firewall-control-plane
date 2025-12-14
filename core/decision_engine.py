from core.policy_engine import match_policy

def decide(risk_score):
    policy = match_policy(risk_score)
    if not policy:
        return {"action": "none", "reason": "Risk below threshold"}

    return {
        "action": policy["action"]["type"],
        "policy": policy["name"],
        "description": policy["description"]
    }

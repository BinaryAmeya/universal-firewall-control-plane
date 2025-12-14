def confidence_level(risk_score, signals):
    if risk_score >= 85 and len(signals) >= 3:
        return "HIGH"
    elif risk_score >= 60 and len(signals) >= 2:
        return "MEDIUM"
    else:
        return "LOW"

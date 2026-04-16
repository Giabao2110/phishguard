from app.schemas.predict import PredictResponse
from app.services.features import UrlFeatures, extract_features


def _score(features: UrlFeatures) -> tuple[float, list[str]]:
    score = 0.0
    explanations: list[str] = []

    if features.url_length > 75:
        score += 20
        explanations.append("Unusually long URL")
    elif features.url_length > 50:
        score += 10
        explanations.append("Moderately long URL")

    if features.domain_length > 30:
        score += 15
        explanations.append("Long domain length")

    if features.dot_count >= 3:
        score += 15
        explanations.append("Many subdomain levels")

    if features.hyphen_count >= 2:
        score += 10
        explanations.append("Multiple hyphens in host")

    if features.digit_count >= 4:
        score += 10
        explanations.append("Many digits in host")

    if features.host_is_ip:
        score += 25
        explanations.append("Host is a raw IP address")

    if features.suspicious_keywords:
        keyword_bonus = min(20, 5 * len(features.suspicious_keywords))
        score += keyword_bonus
        explanations.append(
            f"Suspicious keywords detected: {', '.join(features.suspicious_keywords)}"
        )

    return min(score, 100.0), explanations


def _confidence(risk_score: float) -> float:
    distance_from_mid = abs(risk_score - 50.0)
    confidence = 0.55 + (distance_from_mid / 50.0) * 0.4
    return round(min(confidence, 0.99), 2)


def _verdict(risk_score: float) -> str:
    if risk_score >= 70:
        return "DANGEROUS"
    if risk_score >= 40:
        return "SUSPICIOUS"
    return "SAFE"


def predict_url(url: str) -> PredictResponse:
    features = extract_features(url)
    risk_score, explanations = _score(features)

    if not explanations:
        explanations.append("No high-risk indicators detected by MVP heuristic")

    return PredictResponse(
        verdict=_verdict(risk_score),
        risk_score=round(risk_score, 2),
        confidence=_confidence(risk_score),
        explanations=explanations,
    )

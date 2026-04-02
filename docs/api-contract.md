# API Contract

## AI Service

POST /predict

Request:
{
  "url": "http://secure-paypa1-login.xyz"
}

Response:
{
  "verdict": "DANGEROUS",
  "risk_score": 91.4,
  "confidence": 0.91,
  "explanations": [
    "Suspicious keyword detected",
    "Brand impersonation detected",
    "Abnormal domain structure"
  ]
}
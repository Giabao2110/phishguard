# PhishGuard AI Service (MVP)

FastAPI service providing heuristic phishing URL prediction.

## Run locally

```bash
cd ai-service
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8001
```

## Endpoints

- `GET /health`
- `POST /predict`

### Sample request

```bash
curl -X POST http://localhost:8001/predict \
  -H 'Content-Type: application/json' \
  -d '{"url":"http://secure-paypa1-login.verify-account-update.xyz"}'
```

### Sample response

```json
{
  "verdict": "DANGEROUS",
  "risk_score": 75.0,
  "confidence": 0.75,
  "explanations": [
    "Moderately long URL",
    "Long domain length",
    "Multiple hyphens in host",
    "Suspicious keywords detected: login, verify, secure, update, account"
  ]
}
```

## Notes

- This MVP is deterministic and rule-based.
- No training/inference pipeline or persistence is included.

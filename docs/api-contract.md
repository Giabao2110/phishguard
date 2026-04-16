# PhishGuard MVP API Contract (Frozen)

Last updated: 2026-04-15
Scope: contract between `backend` (Spring Boot) and `ai-service` (FastAPI), plus backend response contract to UI.

## 1) AI Service Contract

### Endpoint
`POST /predict`

### Request (backend -> ai-service)
```json
{
  "url": "http://secure-paypa1-login.xyz"
}
```

### Request Rules
- `url` is required.
- `url` must be a valid absolute URL (`http` or `https`).
- ai-service does not apply whitelist/blacklist logic; that decision is owned by backend.

### Success Response (ai-service -> backend)
```json
{
  "verdict": "DANGEROUS",
  "risk_score": 91.4,
  "confidence": 0.91,
  "explanations": [
    "Suspicious keyword detected",
    "Brand impersonation pattern",
    "Abnormal domain structure"
  ]
}
```

### Success Field Definitions
- `verdict`: enum `SAFE | SUSPICIOUS | DANGEROUS`
- `risk_score`: number in range `0..100` (higher = more dangerous)
- `confidence`: number in range `0..1`
- `explanations`: array of short human-readable strings (can be empty)

---

## 2) Backend Scan Response DTO (backend -> UI)

### Endpoint (MVP)
`POST /api/scans`

### Request (UI -> backend)
```json
{
  "url": "http://secure-paypa1-login.xyz"
}
```

### Success Response DTO
```json
{
  "scanId": "d8e4c1bd-1654-4f9c-9f9b-923353e7f2a7",
  "url": "http://secure-paypa1-login.xyz",
  "verdict": "DANGEROUS",
  "riskScore": 100.0,
  "confidence": 1.0,
  "explanations": [
    "URL is present in blacklist"
  ],
  "sourceDecision": "BLACKLIST",
  "scannedAt": "2026-04-15T09:21:44Z"
}
```

### DTO Field Definitions
- `scanId`: unique identifier for persisted scan history record
- `url`: scanned URL
- `verdict`: enum `SAFE | SUSPICIOUS | DANGEROUS`
- `riskScore`: number in range `0..100`
- `confidence`: number in range `0..1`
- `explanations`: list of displayable explanation strings
- `sourceDecision`: decision source enum (see section 3)
- `scannedAt`: UTC timestamp in ISO-8601 format

---

## 3) `sourceDecision` Enum (Frozen Values)

Allowed values:
- `BLACKLIST` — URL/domain matched blacklist; final decision is immediate.
- `WHITELIST` — URL/domain matched whitelist (only when not blacklisted).
- `AI_SERVICE` — no list override; verdict comes from ai-service prediction.

Precedence (strict):
1. `BLACKLIST`
2. `WHITELIST`
3. `AI_SERVICE`

Interpretation:
- If URL matches blacklist and whitelist simultaneously, backend returns `sourceDecision=BLACKLIST`.
- When source is list-based, backend may set deterministic scores (MVP default):
  - `BLACKLIST` => `verdict=DANGEROUS`, `riskScore=100`, `confidence=1`
  - `WHITELIST` => `verdict=SAFE`, `riskScore=0`, `confidence=1`

---

## 4) Error Response Shape (Frozen)

Used for backend API errors; recommended for ai-service errors as well.

```json
{
  "code": "VALIDATION_ERROR",
  "message": "Request validation failed",
  "fieldErrors": {
    "url": "must be a valid URL"
  }
}
```

### Error Fields
- `code`: stable machine-readable error code
- `message`: human-readable summary
- `fieldErrors`: object map (`field` -> `error message`), empty object when not applicable

### Minimum Error Codes
- `VALIDATION_ERROR` (HTTP 400)
- `BAD_REQUEST` (HTTP 400)
- `AI_SERVICE_UNAVAILABLE` (HTTP 503)
- `INTERNAL_ERROR` (HTTP 500)

---

## 5) MVP Stability Notes

To keep MVP stable and avoid frontend/backend drift:
- Do not rename any fields above.
- Do not change enum spellings/case.
- Keep `riskScore` scale as `0..100` and `confidence` as `0..1`.
- New fields can be added only as optional, never breaking existing clients.

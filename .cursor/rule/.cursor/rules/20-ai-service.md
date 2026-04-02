# AI Service Rule

Applies to: ai-service/**

Use:
- Python 3.10+
- FastAPI
- pandas
- numpy
- scikit-learn
- joblib

Modules:
- app.py
- schemas.py
- services/
- utils/
- models/

Rules:
- keep feature extraction reusable
- keep prediction logic separate from API routes
- support model loading from saved joblib
- return verdict, risk_score, confidence, explanations
- do not introduce deep learning unless explicitly requested
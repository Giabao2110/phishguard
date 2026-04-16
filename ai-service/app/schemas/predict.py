from typing import List, Literal

from pydantic import BaseModel, HttpUrl

Verdict = Literal["SAFE", "SUSPICIOUS", "DANGEROUS"]


class HealthResponse(BaseModel):
    status: str
    service: str


class PredictRequest(BaseModel):
    url: HttpUrl


class PredictResponse(BaseModel):
    verdict: Verdict
    risk_score: float
    confidence: float
    explanations: List[str]

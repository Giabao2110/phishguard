from fastapi import APIRouter

from app.schemas.predict import HealthResponse, PredictRequest, PredictResponse
from app.services.predictor import predict_url

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok", service="ai-service")


@router.post("/predict", response_model=PredictResponse)
def predict(payload: PredictRequest) -> PredictResponse:
    return predict_url(payload.url)

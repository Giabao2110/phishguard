from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json() == {'status': 'ok', 'service': 'ai-service'}


def test_predict_flags_suspicious_url() -> None:
    payload = {'url': 'http://secure-paypa1-login.verify-account-update.xyz'}
    response = client.post('/predict', json=payload)

    assert response.status_code == 200
    body = response.json()
    assert body['verdict'] in {'SUSPICIOUS', 'DANGEROUS'}
    assert body['risk_score'] >= 40
    assert isinstance(body['confidence'], float)
    assert len(body['explanations']) >= 1


def test_predict_safe_url() -> None:
    payload = {'url': 'https://example.com'}
    response = client.post('/predict', json=payload)

    assert response.status_code == 200
    body = response.json()
    assert body['verdict'] == 'SAFE'
    assert body['risk_score'] < 40

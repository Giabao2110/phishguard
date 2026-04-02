# Project Context

Project name: PhishGuard

This is a graduation project about phishing URL detection.

System components:
- backend: Spring Boot + Thymeleaf + PostgreSQL
- ai-service: FastAPI + scikit-learn
- optional cache: Redis

Main workflow:
1. user submits a URL
2. backend checks whitelist/blacklist
3. backend performs basic rule checks
4. backend calls ai-service
5. ai-service returns verdict + risk score + explanations
6. backend stores scan history
7. UI shows final result

Core outputs:
- SAFE / SUSPICIOUS / DANGEROUS
- risk_score
- explanation list
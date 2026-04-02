# PhishGuard Project Rule

Project: PhishGuard
Goal: Build an AI-powered web platform for real-time phishing URL detection.

Tech stack:
- Backend: Java Spring Boot, Thymeleaf, PostgreSQL
- AI service: Python FastAPI, scikit-learn
- Optional cache: Redis

Architecture:
- backend and ai-service are separate services
- backend calls ai-service via HTTP
- PostgreSQL stores users, scan history, blacklist, whitelist
- Thymeleaf is used for fast MVP UI

Primary features:
- login/register
- URL scan
- risk score + explanation
- scan history
- admin dashboard
- blacklist/whitelist management
- brand impersonation detection

Constraints:
- do not switch frameworks
- do not over-engineer
- keep layered architecture
- keep backend and ai-service independent
- prioritize working MVP first
- when fixing bugs, make the minimum necessary changes
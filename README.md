# PhishGuard

Dự án phát hiện / phòng chống phishing (backend, AI service, tài liệu và dữ liệu).

## Cấu trúc

| Thư mục / file | Mô tả |
|----------------|--------|
| `backend/` | API và logic ứng dụng chính |
| `ai-service/` | Dịch vụ ML / inference |
| `docs/` | Tài liệu kỹ thuật, báo cáo |
| `datasets/` | Dữ liệu huấn luyện / đánh giá |
| `scripts/` | Script tiện ích (ETL, deploy, v.v.) |
| `.env` | Biến môi trường (không commit bí mật) |
| `docker-compose.yml` | Chạy stack bằng Docker |

## Bắt đầu

1. Sao chép `.env` và điền giá trị phù hợp.
2. Cấu hình `docker-compose.yml` khi đã có Dockerfile trong `backend` / `ai-service`.
3. Xem thêm trong `docs/`.

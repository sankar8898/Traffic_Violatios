
# 🚦 Traffic Violation Management Microservice

## 🔧 Tech Stack
- Python 3.10
- Django
- PostgreSQL
- Docker
- REST Framework
- Requests (for S3 image validation)
- `.env` config management

---

## 🚀 API Endpoints

### 1. POST /violations/ingest
Creates a violation record.

**Required JSON:**
```json
{
  "license_plate": "TS09EX1234",
  "violation_type": "Signal Jump",
  "violation_image_url": "https://s3.amazonaws.com/fine-images/image123.jpg",
  "violation_datetime": "2025-07-15T18:30:00Z",
  "location": "Hyderabad - Gachibowli Junction"
}

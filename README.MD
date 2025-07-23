cat > README.md << 'EOF'
# 🚦 Traffic Violation Management System

## 📘 Project Overview

This Django-based microservice ingests, stores, and retrieves traffic violation data from IoT cameras. It handles AWS S3 image validation, PostgreSQL storage, REST APIs, and is fully containerized with Docker.

---

## 📁 Environment Variables (.env)

Place this `.env` file in your root directory:

DB_NAME=Traffic_Violation_db
DB_USER=postgres
DB_PASSWORD=Geetha@29
DB_HOST=pg_violation
DB_PORT=5432

S3_BASE_URL=https://s3.amazonaws.com/fine-images/
IMAGE_HOST=https://cdn-icons-png.flaticon.com

DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

yaml
Copy
Edit

---

## 🐳 Docker & Django Setup (Step-by-Step)

### 1️⃣ Create Docker Network

```
docker network create traffic_net
2️⃣ Start PostgreSQL Container
bash
Copy
Edit
docker run -d \
  --name pg_violation \
  --network traffic_net \
  -e POSTGRES_DB=Traffic_Violation_db \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=Geetha@29 \
  -p 5432:5432 \
  postgres
3️⃣ Build Django Docker Image

docker build -t traffic_violation_service2 .
4️⃣ Run Django Container

docker run -it \
  -p 8000:8000 \
  --env-file .env \
  --network traffic_net \
  traffic_violation_service2
Visit the app at: http://localhost:8000

5️⃣ Apply Migrations (Inside Running Django Container)

docker ps  # Find container name or ID
docker exec -it <container_name> python manage.py migrate
6️⃣ Create Superuser

docker exec -it <container_name> python manage.py createsuperuser
🔗 API Endpoints
Method	Endpoint	Description
POST	/violations/ingest/	Ingest violation data
GET	/violations/<license_plate>/	Get violations by license plate
PATCH	/violations/<id>/update-status/	Update status (e.g., mark as paid)

🔐 Django Admin
URL: http://localhost:8000/admin

Login with your created superuser credentials

✅ Optional Features Implemented
Django signals for event logging

AWS S3 image URL validation via HEAD request

Environment variable config using .env

Docker-based deployment

Logs accessible using docker logs

🧰 Helpful Docker Commands

# List running containers
docker ps

# Stop a container
docker stop <container_name>

# Remove a container
docker rm <container_name>

# Exec into a container shell
docker exec -it <container_name> bash

# View container logs
docker logs <container_name>

# Inspect Docker network
docker network inspect traffic_net
📦 Final Checklist
 PostgreSQL container running

 Django container running

 Docker network connected

 .env environment variables loaded

 Migrations applied

 Superuser created

 APIs tested and working

📂 Folder Structure

Traffic_Violation_Management/
├── violations/              # Django app logic
├── manage.py
├── Dockerfile
├── requirements.txt
├── .env
└── README.md

👩‍💻 Author
Sankar y
 
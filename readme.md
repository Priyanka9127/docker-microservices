# Microservices Application with Docker Compose 🚀

## Introduction 📢

This project demonstrates a **microservices-based application** built using **Docker** and **Docker Compose**. The application consists of the following core services:

- **🌍 Web Service (Flask App)** - Handles HTTP requests and provides a user interface.
- **⚙️ Worker Service (Celery & Redis)** - Processes background tasks asynchronously.
- **🗄 Database Service (PostgreSQL)** - Stores persistent data.
- **🔥 Redis (Broker)** - Facilitates message communication for task management.

This setup showcases containerization, orchestration, and microservices architecture skills.

![Microservices Architecture](https://upload.wikimedia.org/wikipedia/commons/1/1c/Microservices.png)

## Features ✨

- **🔗 Microservices Architecture** - Independent and scalable services.
- **🐳 Dockerized Services** - Ensures consistency across environments.
- **📦 Docker Compose for Orchestration** - Simplifies multi-container management.
- **⚡ Asynchronous Processing** - Uses Celery and Redis for task management.
- **💾 Data Persistence** - Ensures database durability via Docker volumes.
- **🌐 Web UI** - Flask-based interface for user interactions.
- **🖥️ Custom Image Names** - Prefixes container names with `docker_microservices`.
- **🚀 Exposed Web Service** - Available at [http://localhost:8080](http://localhost:8080).
- **📜 Verified Communication** - Logs and interactions ensure container connectivity.

## Skills Demonstrated 🏆

- **🛠 Microservices Design** - Independent, loosely coupled services.
- **🐳 Docker & Docker Compose** - Containerization & multi-container orchestration.
- **🌍 Flask Web Development** - Backend web service implementation.
- **⚙️ Celery for Async Tasks** - Background job processing.
- **🔥 Redis as Message Broker** - Efficient task management.
- **🗄 PostgreSQL Database** - Persistent data storage.
- **🔗 Container Networking** - Communication between services.
- **📊 Log Management** - Monitoring application behavior.

## Architecture Diagram 🏗

```
+-------------------+      +--------------------+      +---------------------+
| Web Service      | <---> | Redis (Broker)    | <---> | Worker Service     |
| (Flask App)      |      |                    |      | (Celery Worker)     |
| - Exposes port 8080 |    +--------------------+      | - Background Tasks  |
+-------------------+                                  +---------------------+
        |
        v
+-------------------+
| Database Service |
| (PostgreSQL)     |
| - Persistent Data|
+-------------------+
```

## Getting Started 🚀

### Prerequisites 📌

- **🐳 Docker** - Install from [Docker Desktop](https://www.docker.com/products/docker-desktop).
- **📦 Docker Compose** - Verify with:

```sh
docker-compose --version
```

### Installation & Setup ⚙️

**1. Clone the repository:**

```sh
git clone <your_repository_url>
cd docker_microservices
```

Ensure the file structure:

```
docker_microservices/
├── docker-compose.yml
├── web-service/
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
│   └── templates/
│       └── index.html
└── worker-service/
    ├── Dockerfile
    ├── requirements.txt
    └── worker.py
```

**2. Build Docker Images:**

```sh
docker-compose build
```

**3. Start the Application:**

```sh
docker-compose up -d
```

## Verification 🔍

### Access Web Service 🌐

Open [http://localhost:8080](http://localhost:8080) in your browser. You should see:

- **"Hello from Web Service!"** 🎉
- **Your Name** 🏷️
- **Your Roll Number** 🆔
- **Your Bio** 📜
- **Web Service Container ID** 🔢
- **Current Time** ⏳

### Check Logs 📜

- **Web Service Logs:**

```sh
docker-compose logs web
```

- **Worker Service Logs:**

```sh
docker-compose logs worker
```

- **Database Logs:**

```sh
docker-compose logs db
```

- **Redis Logs:**

```sh
docker-compose logs redis
```

### Check Running Containers ✅

```sh
docker ps
```

You should see the following running services:

- `docker_microservices-web-service` 🌐
- `docker_microservices-worker-service` ⚙️
- `postgres:13` 🗄
- `redis:latest` 🔥

## Repository Structure 📂

```
docker_microservices/
├── docker-compose.yml         # Docker Compose file
├── web-service/               # Web Service Directory
│   ├── Dockerfile             # Web Service Dockerfile
│   ├── app.py                 # Flask Application
│   ├── requirements.txt       # Dependencies
│   └── templates/             # HTML Files
│       └── index.html         # Web UI
└── worker-service/            # Worker Service Directory
    ├── Dockerfile             # Worker Dockerfile
    ├── requirements.txt       # Dependencies
    └── worker.py              # Celery Worker Code
```

## License 📜

[MIT License](https://opensource.org/licenses/MIT)


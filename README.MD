# 📌 **Event and Notification Management System**

This project is a **REST API** built with **Django, DRF, and Celery** that allows managing events, registrations, and
asynchronous notifications.

## 🚀 **Installation and Execution**

### **1️⃣ Clone the repository**

```bash
git clone https://github.com/Silversun31/Tech-Test--Event-and-Notification-Management-System
cd "Tech-Test--Event-and-Notification-Management-System"
```

### 2️⃣ Create and activate a virtual environment

```bash
python -m venv venv
# On linux
source venv/bin/activate  
# On Windows: 
venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure environment variables

Create a .env file based on `./docs/deploy/environments/local.env` file and configure the parameters.
> [!IMPORTANT]
> It is important that the environment file should be named `.env`, if you are copying the `local.env`
> file, make sure to remove the `local` initial string.

> [!IMPORTANT]
> The `.env` file should be in the root of the project.

### 5️⃣ Apply migrations and create a superuser

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 6️⃣ Start the servers

```bash
# Redis
docker run --name redis -p 6379:6379 -d redis

# Celery
# You can execute run_celery.bat file, or run the next command in the terminal:
.\venv\Scripts\activate && celery -A config worker --loglevel=info --pool=solo

# Django
python manage.py runserver
```

### 7️⃣ Access the API

* Swagger: http://127.0.0.1:8000/swagger/
* Notifications: /api/notifications/
* Events: /api/events/
* Registrations: /api/registrations/

---

## 🧪 Running Tests

```bash
pytest
```

## Celery troubleshooting 🐇

Running Celery step by step:

### Install redis:

#### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install redis-server -y
sudo systemctl enable redis
sudo systemctl start redis
```

#### macOS (Homebrew)

```bash
brew install redis
brew services start redis
```

#### Windows (Docker)

> [!TIP]  
> Please be sure that docker engine is running

```bash
docker run --name redis -p 6379:6379 -d redis
```

### To run celery worker:

You can execute the run_celery.bat file, or run the next command in the terminal:

```bash
.\venv\Scripts\activate && celery -A config worker --loglevel=info
```
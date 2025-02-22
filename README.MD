## Run Celery step by step:

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
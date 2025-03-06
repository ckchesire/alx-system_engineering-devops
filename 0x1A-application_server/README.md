# 0x1A-application_server

# Gunicorn Deployment Guide

## Overview
Gunicorn (Green Unicorn) is a WSGI HTTP server for running Python web applications efficiently. It is commonly used with Flask and Django in production environments.

---

## Installation
Install Gunicorn using pip:

```bash
pip install gunicorn
```

Verify installation:

```bash
gunicorn --version
```

---

## Running a Flask App with Gunicorn

### Step 1: Create a Flask App (`app.py`)

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Gunicorn!"

if __name__ == "__main__":
    app.run()
```

### Step 2: Start the Application

```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```
- `-w 4`: 4 worker processes.
- `-b 0.0.0.0:8000`: Binds to port 8000.
- `app:app`: First `app` is the filename, second `app` is the Flask instance.

---

## Running a Django App with Gunicorn

Navigate to the Django project directory and run:

```bash
gunicorn -w 4 -b 0.0.0.0:8000 myproject.wsgi
```
Replace `myproject.wsgi` with your project's WSGI module.

---

## Running Gunicorn as a Background Process

```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app --daemon
```

To stop Gunicorn:

```bash
pkill gunicorn
```

---

## Configuring Gunicorn with a Config File
Create a `gunicorn.conf.py` file:

```python
workers = 4
bind = "0.0.0.0:8000"
timeout = 120
accesslog = "gunicorn_access.log"
errorlog = "gunicorn_error.log"
```
Run Gunicorn with the config file:

```bash
gunicorn -c gunicorn.conf.py app:app
```

---

## Running Gunicorn as a Systemd Service (Linux)

Create a service file at `/etc/systemd/system/gunicorn.service`:

```ini
[Unit]
Description=Gunicorn instance to serve Flask/Django app
After=network.target

[Service]
User=youruser
Group=www-data
WorkingDirectory=/path/to/your/app
ExecStart=/path/to/venv/bin/gunicorn -w 4 -b 0.0.0.0:8000 app:app

[Install]
WantedBy=multi-user.target
```

Reload systemd and start the service:

```bash
sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
```

---

## Running Gunicorn Behind Nginx

Example Nginx config:

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

Restart Nginx:

```bash
sudo systemctl restart nginx
```

---

## Conclusion
Gunicorn is a powerful WSGI server for deploying Python web applications. It is commonly used with Nginx for a scalable and production-ready setup.

For advanced usage, consider containerizing Gunicorn in Docker.

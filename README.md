![CI](https://github.com/izakh13/taskly/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.14.4-blue)
![Django](https://img.shields.io/badge/Django-6.1.1-green)
# TASKLY
Simple task manager

### TECHNOLOGIES:
* Django
* DRF
* Postgresql
* Docker
* Gemini API
* pytest
* Github Actions
* Render

### URLs
* [Simple web interface](https://taskly-xpjl.onrender.com/tasks/)
* [Browsable API](https://taskly-xpjl.onrender.com/api/tasks/)

### FEATURES
* Show list of tasks
* Create new task
* Improve task description using Gemini API

### How to run locally
Create a `.env` file based on `.env.example` and fill in your own values (including GEMINI_API_KEY)
```bash
git clone https://github.com/izakh13/taskly.git
cd taskly
docker-compose up --build
```
**ALL URLs are insecure. Everyone can create, delete, update tasks**
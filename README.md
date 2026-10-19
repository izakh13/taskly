![CI](https://github.com/izakh13/taskly/actions/workflows/ci.yml/badge.svg)
![codecov](https://codecov.io/gh/izakh13/taskly/branch/main/graph/badge.svg)
![Python](https://img.shields.io/badge/Python-3.14.4-blue)
![Django](https://img.shields.io/badge/Django-6.1.1-green)
# TASKLY
Simple task manager

### TECHNOLOGIES
#### BACKEND AND DATA
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Django REST](https://img.shields.io/badge/Django%20REST-D32F2F?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
#### AI
![GeminiAPI](https://img.shields.io/badge/Gemini%20API-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white)
#### FRONTEND
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
#### CONTAINERS AND DEPLOY
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Render](https://img.shields.io/badge/Render-000000?style=for-the-badge&logo=render&logoColor=white)
#### TESTS AND CI
![pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)
![Codecov](https://img.shields.io/badge/Codecov-F01F7A?style=for-the-badge&logo=codecov&logoColor=white)

### URLs

> [!WARNING]
>
> The live demo runs on a free hosting plan and goes to sleep when inactive. The first request after a pause can take about a minute to respond.

* [Simple web interface](https://taskly-xpjl.onrender.com/tasks/)
* [Browsable API](https://taskly-xpjl.onrender.com/api/tasks/)

### FEATURES
* Show list of tasks
* Create new task
* Improve task description using Gemini API
* Edit, delete task

### How to run locally
Create a `.env` file based on `.env.example` and fill in your own values (including GEMINI_API_KEY)
```bash
git clone https://github.com/izakh13/taskly.git
cd taskly
docker compose up --build
```
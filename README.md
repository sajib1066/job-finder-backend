# job-finder-backend
[![django-version](https://img.shields.io/badge/django-3.1-green)](https://www.djangoproject.com/)
[![python-version](https://img.shields.io/badge/python-3.8-blue)](https://www.python.org/)
[![mysql-version](https://img.shields.io/badge/mysql-8.0.21-orange)](https://www.mysql.com/)
[![GH-Actions](https://github.com/sajib1066/job-finder-backend/workflows/JOB_FINDER_BACKEND_CI/badge.svg)](https://github.com/sajib1066/job-finder-backend/actions)

Pull Docker Image

```
docker pull sajib1066/job-finder-backend:latest
```

Run Project With Docker

```
docker run -d -p 8000:8000 sajib1066/job-finder-backend:latest
```

Create User

```
docker exec -it <container_id> python manage.py createsuperuser
```

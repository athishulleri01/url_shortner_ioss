# 🚀 Django URL Shortener

A simple yet powerful **URL Shortener** built with Django, featuring:
- Short URL generation
- Redirection to the original link
- Click tracking & statistics
- REST API endpoint for programmatic use
- Dockerized setup for easy deployment

---

## 📌 Features
- Shorten long URLs into clean, shareable links.
- Redirect short links to their original destination.
- Click analytics for each short code.
- REST API for integration into other apps.
- Fully containerized with **Docker Compose**.

---

## 🛠️ Tech Stack
- **Backend:** Django, Django REST Framework
- **Database:** PostgreSQL
- **Frontend:** Bootstrap 5
- **Reverse Proxy:** Nginx
- **Containerization:** Docker & Docker Compose

---
## Project Structure

```
url_shorter/
├── config/
│   ├── __init__.py
│   ├── urls.py
│   ├── wsgi.py
|   └── settings/
|      ├── __init__.py
|      ├── base.py
|      ├── local.py
|      └── production.py
├── core_apps/
│   ├── __init__.py
│   ├── urlshortner/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── forms.py
├── docker/
│   ├── local/
│   ├── production/
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── signin.html
├── static/
├── requirements/
|    ├── base.txt
|    ├── local.txt
|    └── production.txt
├── .envs/
|    ├── .env.example
|    ├── .env.local
├── manage.py
├── README.md
```

---

## ⚙️ Prerequisites
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## 🚀 Getting Started

### 1 Clone the Repository
```bash
git clone https://github.com/your-username/url-shortener.git
cd url-shortener
```

### 2 Run 
```bash
docker compose -f local.yml up --build -d --remove-orphans
```

### 3 Access with help of browser
```bash
localhost:8080/
```

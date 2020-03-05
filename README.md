# Eticket

Eticketing system

### Requirements

- Python = 3.8.1
- Docker Use [Docker CE](https://docs.docker.com/engine/installation) for Linux or [Docker Toolbox](https://www.docker.com/products/docker-toolbox) for Windows and Mac.

### Setting up Project

- Install all project dependencies with virtual environtment.

```bash
# create virtual environtment
virtualenv venv
# activate environtment
. venv/bin/activate
# install dependency
pip install -r requirements.txt
```

### How to Run

- Eticket system requires PostgreSQL.
- Run PostgreSQL using docker compose.

```bash
docker-compose up -d
```

- Migrate database and run

```bash
# migrate database
python manage.py db upgrade
# seed database
python manage.py seed
# run server
python manage.py run
```

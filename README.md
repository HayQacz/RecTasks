Quick setup:

Clone the repo:
```bash
git clone https://github.com/HayQacz/RecTasks
```

From the root folder of the project run:
```bash
docker-compose up --build -d
```

then 

```bash
docker-compose exec web python manage.py migrate
```

App should be running on `localhost:8000`

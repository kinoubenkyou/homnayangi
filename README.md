# homnayangi

## development

### config

```shell
LC_CTYPE=C sh -c "tr -dc [:alnum:] < /dev/urandom | head -c 50 > django_secret_key"
LC_CTYPE=C sh -c "tr -dc [:alnum:] < /dev/urandom | head -c 20 > postgres_password"
docker compose run --rm app sh -c "python manage.py migrate"
```

### start

```shell
docker compose up -d
```

### stop

```shell
docker compose stop
```

### shell

```shell
docker compose run --no-deps --rm app sh
```

### add package

```shell
docker compose run --no-deps --rm app sh -c "pip install <package> && pip freeze > requirements.txt"
docker compose build
docker compose down -v
```

# homnayangi

## development

### configurate

```shell
docker compose run --no-deps --rm app sh -c "python generate_secret_key.py > django_secret_key"
LC_CTYPE=C sh -c "tr -dc [:alnum:] < /dev/urandom | head -c 20 > postgres_password"
chmod 600 django_secret_key postgres_password
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

## lint and format

```shell
docker compose run --no-deps --rm app sh -c "ruff check --fix --unsafe-fixes"
docker compose run --no-deps --rm app sh -c "ruff format --preview"
```

## test

```shell
docker compose run --rm app sh -c "python manage.py test"
```

## production

### build

```shell
docker build -f production.Dockerfile -t public.ecr.aws/d1p6t0r8/homnayangi-app .
```

### push

```shell
docker push public.ecr.aws/d1p6t0r8/homnayangi-app:latest
```

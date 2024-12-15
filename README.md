# homnayangi

## development

### dependencies

- python 3.13.0
- postgres
- chromium

### configure

1. run

```shell
cp .env-sample .env
```

2. fill `.env`
3. run

```shell
pip install -r requirements.txt
python manage.py migrate
```

### start

```shell
python manage.py runserver
```

### add package

```shell
pip install <package> && pip freeze > requirements.txt
```

### lint and format

```shell
ruff check --fix --unsafe-fixes
ruff format --preview
```

### test

```shell
python manage.py test
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

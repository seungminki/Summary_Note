## Docker-Compose
```Python
# docker-compose.yml

version: "3.9"
services:
  web:
    build: .
    ports:
    - "5000"
  redis:
    image: "redis:alpine"
```
```Python
# Dockerfile

FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]
```
```Python
# app.py

import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)
```
```Python
#requirements.txt

flask
redis
```
```Python
# mkdir workspace 라는 폴더를 만들어서
# nano 로 각 파일을 만듦
# docker desktop이 깔려있어서 새로 설치할 필요는 없었다
# docker-compose -v 로 버전 확인
# Dockerfile로 포트 변경 가능( 지정하지 않을 경우 랜덤 설정)
```
```Python
seungmin@WIN-O8SINOSHT17:~/docker/workspace2$ docker ps
CONTAINER ID   IMAGE            COMMAND                  CREATED         STATUS          PORTS                     NAMES
9f65714695de   redis:alpine     "docker-entrypoint.s…"   5 minutes ago   Up 10 seconds   6379/tcp                  workspace2-redis-1
4e8b6b4e099e   workspace2-web   "flask run"              5 minutes ago   Up 10 seconds   0.0.0.0:56039->5000/tcp   workspace2-web-1
# 5000번 포트 아니고 56039 포트임
```
```Python
$ docker-compose up
# docker-compose 실행

$ docker-compose up -d
# 백그라운드에서 실행

$ docker-compose down
# 종료

$ docker-compose down -v
# 삭제

$ docker-compose -p my-project up --scale web=3 (-d)
# 3개로 확장

$ docker stop $(docker ps -a -q)
# 다 꺼버리기
```

## Docker 실습 - Docker compose
1. docker compose  
2. Docker compose from Dockerfile  
1) Jupyter Notebook   환경만들기  
  1-2) 추가 요구사항   
    2) My-SQL 환경 만들기  
    3) MongoDB 만들고 CRUD 하기  

* docker compose 로 jupyter notebook 실행할 수 있는 환경을 만들어 봅니다.
* 요구사항
  * jupyter notebook의 기본 포트는 8888

```Python
# Dockerfile

FROM python:3.8
WORKDIR /code
RUN python -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8888
COPY . /code
ENTRYPOINT ["jupyter"]
CMD ["notebook", "--ip", "0.0.0.0", "--port", "8888", "--allow-root", "--NotebookApp.token='password'"]
```
```Python
# docker-compose.yml
version: "3"
services:
    web:
        build: .
        ports:
            - "8888:8888"
        volumes:
            - .:/workspace4
        container_name: ct-jupyter
```

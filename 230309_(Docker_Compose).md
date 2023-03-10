## Docker-Compose
```Python
# mkdir workspace 라는 폴더를 만들어서
# nano 로 각 파일을 만듦
# docker desktop이 깔려있어서 새로 설치할 필요는 없었다
# docker-compose -v 로 버전 확인
# Dockerfile로 포트 변경 가능( 지정하지 않을 경우 랜덤 설정)

seungmin@WIN-O8SINOSHT17:~/docker/workspace2$ docker ps
CONTAINER ID   IMAGE            COMMAND                  CREATED         STATUS          PORTS                     NAMES
9f65714695de   redis:alpine     "docker-entrypoint.s…"   5 minutes ago   Up 10 seconds   6379/tcp                  workspace2-redis-1
4e8b6b4e099e   workspace2-web   "flask run"              5 minutes ago   Up 10 seconds   0.0.0.0:56039->5000/tcp   workspace2-web-1
# 5000번 포트 아니고 56039 포트임

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
# 모든 컨테이너 정지하기

$ docker rm $(docker ps -a -q)
# 모든 컨테이너 삭제하기

$ docker-compose up --build --force-recreate -d
--build: 변경된 이미지를 다시 build
--force-recreate: docker-compose up 을 하면 변경된 사항을 적용하여 컨테이너를 재 생성하지만 up 을 했을때에도 변경이 적용이 안되는 경우에 해당 옵션을 주어보자.
-d: Run containers in the background
# 컨테이너 업데이트

# docker-compose 설치
$ sudo curl -L "https://github.com/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
$ sudo chmod +x /usr/local/bin/docker-compose
$ sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

# sudo 없이 docker 쓰기
sudo usermod -aG docker ${USER}
sudo su
su - ubuntu
groups ubuntu
docker run hello-world
```

### flask
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

### jupyter-notebook
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

### 다른 포트로 docker-compose 2개 만들기
```Python
# docker-compose.yml

version: "3.9"
services:
    jupyter-ds:
        build:
            context: ${PWD}/jupyter-ds
            dockerfile: ${PWD}/jupyter-ds/Dockerfile
        ports:
            - "8890"
        volumes:
            - ${PWD}/jupyter-ds:/app
        restart: always

    jupyter-engineer:
        build:
            context: ${PWD}/jupyter-engineer
            dockerfile: ${PWD}/jupyter-engineer/Dockerfile
        ports:
            - "8899"
        volumes:
            - ${PWD}/jupyter-engineer:/app
        restart: always
```
### mysql
```Python
# docker-compose.yml
version: "3"

services:
    mysql:
        image: mysql:5.7
        volumes:
            - db_volume:/var/lib/mysql
        environment:
            MYSQL_DATABASE: my-services
            MYSQL_USER: test-user
            MYSQL_PASSWORD: 12345!
            MYSQL_ROOT_PASSWORD: 12345!

volumes:
    db_volume:
```
```Python
# mysql container 접속
$ docker exec -it work30_mysql_1 bash
# mysql -u root -p
Enter password: 12345!
mysql>

# 데이터베이스 조회
show databases;

# 데이터베이스 선택
use mysql;

# 테이블 조회
show tables;

# 데이터 보기
select user, host from user;
+---------------+-----------+
| user          | host      |
+---------------+-----------+
| root          | %         |
| test-user     | %         |
| mysql.session | localhost |
| mysql.sys     | localhost |
| root          | localhost |
+---------------+-----------+
5 rows in set (0.00 sec)
select * from user;

```

### mongodb
```Python
# docker-compose.yml
version: '3.8'

services:
  mongodb:
    image: mongo
    container_name: mongodb
    restart: always
    ports:
      - 27017:27017
    volumes:
      - ./mongodb:/data/db
    environment:
      - MONGO_INITDB_ROOT_USERNAME=root
      - MONGO_INITDB_ROOT_PASSWORD=1234 
      - MONGO_INITDB_DATABASE=mydb
```
```Python
# docker ps
CONTAINER ID   IMAGE       COMMAND                  CREATED          STATUS          PORTS                               NAMES
2a71c89dfbcd   mongo       "docker-entrypoint.s…"   20 seconds ago   Up 19 seconds   0.0.0.0:27017->27017/tcp            mongodb

# mongodb 접속
mongosh -u root -p 1234

# 컨테이너 접속
docker exec -it mongodb /bin/bash

# database 변경
> use mydb
switched to db mydb

# collection 생성
> db.createCollection('book')
{ "ok" : 1 }

# 데이터 입력
> db.book.insertOne({name:"hello mongo", author:"choi"})
{
        "acknowledged" : true,
        "insertedId" : ObjectId("61e374229cbbcefe0d6d744b")
}

> db.book.insertMany([{name:"hello java", author:"kim"}, {name:"hello docker", author:"lee"}])
{
        "acknowledged" : true,
        "insertedIds" : [
                ObjectId("61e374779cbbcefe0d6d744c"),
                ObjectId("61e374779cbbcefe0d6d744d")
        ]
}

# 데이터 조회
> db.book.find().pretty()
{
        "_id" : ObjectId("61e374229cbbcefe0d6d744b"),
        "name" : "hello mongo",
        "author" : "choi"
}
{
        "_id" : ObjectId("61e374779cbbcefe0d6d744c"),
        "name" : "hello java",
        "author" : "kim"
}
{
        "_id" : ObjectId("61e374779cbbcefe0d6d744d"),
        "name" : "hello docker",
        "author" : "lee"
}

# 데이터 업데이트
> db.book.updateOne( { _id: ObjectId("61e374779cbbcefe0d6d744d") }, { $set: { author: "lee docker" } } )
{ "acknowledged" : true, "matchedCount" : 1, "modifiedCount" : 1 }

# 업데이트 데이터 조회
> db.book.find({name:"hello docker"})
{ "_id" : ObjectId("61e374779cbbcefe0d6d744d"), "name" : "hello docker", "author" : "lee docker" }

# 데이터 삭제
> db.book.deleteOne({name:"hello docker"})
{ "acknowledged" : true, "deletedCount" : 1 }
> db.book.find()
{ "_id" : ObjectId("61e374229cbbcefe0d6d744b"), "name" : "hello mongo", "author" : "choi" }
{ "_id" : ObjectId("61e374779cbbcefe0d6d744c"), "name" : "hello java", "author" : "kim" }
```

# ai
AI &amp; Machine Learning Package - Python


## Usage:

### Python

```
git clone git@github.com:d0nQuix0t3/ai.git
```

```
cd ai
```

```
python3 -m pip install --upgrade pip setuptools wheel
```

```
python3 setup.py sdist bdist_wheel
```

```
python3 -m pip install .
```

### Docker

**File Structure**
```
|-PyPackager
    |-Dockerfile
    |-docker-compose.yml
```

**Dockerfile**
```
FROM python:3.7-alpine
RUN apk update && apk upgrade && apk add --no-cache git 

RUN git clone https://github.com/d0nQuix0t3/ai.git
WORKDIR  /ai

RUN python -m pip install --upgrade pip setuptools wheel
RUN python setup.py sdist bdist_wheel 
RUN python -m pip install . 
ENTRYPOINT [ "python" ]
```

**docker-compose.yml**
```
---
version: '3.3'
services:
  python-packager:
    build: .
    stdin_open: true
    tty: true
    entrypoint: /bin/sh
```
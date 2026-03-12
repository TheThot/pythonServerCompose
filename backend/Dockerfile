FROM python:3

WORKDIR /usr/src/app

RUN apt-get update && pip install --no-cache-dir fastapi uvicorn

COPY . .

CMD [ "python", "./main.py" ]
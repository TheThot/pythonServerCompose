FROM python:3-slim

RUN apt-get update && pip install --no-cache-dir fastapi uvicorn

RUN groupadd -r myappgroup && useradd -r -g myappgroup -m -s /bin/bash userbackend

USER userbackend

WORKDIR /app

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=5 \
  CMD curl -f http://localhost:8080 || exit 1

COPY . .

CMD [ "python", "./main.py" ]
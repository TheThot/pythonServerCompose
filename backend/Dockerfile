FROM python:3-slim

RUN apt-get update && apt-get install -y curl && pip install --no-cache-dir fastapi uvicorn

RUN groupadd -r myappgroup && useradd -r -g myappgroup -m -s /bin/bash userbackend

USER userbackend

WORKDIR /app

EXPOSE $BACKEND_PORT

HEALTHCHECK --interval=15s --timeout=3s --start-period=20s --retries=3 \
  CMD curl -f http://localhost:$BACKEND_PORT || exit 1

COPY . .

CMD python ./main.py $BACKEND_PORT
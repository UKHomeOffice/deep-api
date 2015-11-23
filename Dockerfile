FROM alpine:3.2
MAINTAINER Ivan Pedrazas <ipedrazas@gmail.com>

RUN apk add --update \
      python \
      py-pip \
      jq \
      curl \
      bash && \
      pip install eve flask-cors

COPY api /app


CMD [ "python", "/app/api.py" ]

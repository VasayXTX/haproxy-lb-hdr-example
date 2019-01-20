FROM python:3.7-alpine3.8

RUN apk update \
    && apk add --no-cache git openssh-client \
    && pip install pipenv \
    && addgroup -S -g 1001 app \
    && adduser -S -D -h /app -u 1001 -G app app

RUN mkdir /app/src
WORKDIR /app/src
COPY Pipfile Pipfile.lock server.py /app/src/

RUN chown -R app:app /app
USER app
RUN pipenv install

ENTRYPOINT ["pipenv", "run", "python", "server.py"]

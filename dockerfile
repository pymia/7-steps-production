FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

RUN pip install --upgrade pip pipenv
WORKDIR /app
COPY . /app
RUN pipenv install --system --deploy

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
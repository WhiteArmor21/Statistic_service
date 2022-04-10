FROM python:3.8.3-alpine

WORKDIR /ciplay

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERRED=1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./req.txt .
RUN pip install -r req.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/ciplay/entrypoint.sh"]
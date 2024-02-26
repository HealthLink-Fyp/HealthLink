FROM python:3.10.10-alpine AS backend

WORKDIR /app/

COPY poetry.lock pyproject.toml /app/

# psycopg2 prerequisites
RUN apk add --no-cache postgresql-dev gcc g++ python3-dev


RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi --no-root && \
    # remove cache to reduce image size
    rm -rf /root/.cache 

RUN touch /app/README.md

COPY . /app/

EXPOSE 8000

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
FROM python:3.10.10-alpine AS backend

WORKDIR /app/

COPY poetry.lock pyproject.toml /app/

# For pg_config executable to be available
RUN apk --no-cache add "postgresql-dev" "gcc" "g++"

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi

RUN touch /app/README.md

COPY . /app/

EXPOSE 8000

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
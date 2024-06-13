FROM python:3.11-slim

# Set work directory
WORKDIR /drf

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc build-essential libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install psycopg2-binary \
    && pip install --no-cache-dir -r requirements.txt \
    && python -m spacy download en_core_web_lg \
    && pip install gunicorn 

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1   
ENV DJANGO_SETTINGS_MODULE healthlink.settings.prod
ENV PORT 8000

# Copy application code
COPY . .

# Django essentials
RUN python manage.py makemigrations --noinput \
    && python manage.py migrate --run-syncdb --noinput \
    && python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "healthlink.wsgi:application"]


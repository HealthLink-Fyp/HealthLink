FROM python:3.11-slim

# Set work directory
WORKDIR /drf

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential \
    && apt-get purge -y --auto-remove build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip \
    && python -m spacy download en_core_web_lg \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install gunicorn
    
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1   
ENV DJANGO_SETTINGS_MODULE healthlink.settings.local
ENV PORT 8000

# Copy application code
COPY . .

# Django essentials
RUN python manage.py makemigrations --noinput \
    && python manage.py migrate --run-syncdb --noinput \
    && python manage.py collectstatic --noinput

# Expose port 8000
EXPOSE 8000

# Define the default command to run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "healthlink.wsgi:application", "--timeout", "300"]



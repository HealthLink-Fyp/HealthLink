FROM python:3.11-slim

# Install dependencies
COPY requirements.txt ./
RUN apt-get update && apt-get clean && apt-get autoremove
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN python3 -m spacy download en_core_web_lg
RUN pip install gunicorn

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1   
ENV DJANGO_SETTINGS_MODULE healthlink.settings.local
ENV PORT 8000

# Copy application code
COPY . .

# Static files
RUN python manage.py collectstatic --noinput

# Migrate database
RUN python manage.py migrate --noinput

# Expose port 8000
EXPOSE 8000

# Define the default command to run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "healthlink.wsgi:application", "--timeout", "300"]

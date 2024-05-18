FROM python:3.11-slim

# Install dependencies
RUN apt-get update && apt-get install -y python3-opencv && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy requirements and install python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Perform database migrations
RUN python3 manage.py makemigrations && python3 manage.py migrate --run-syncdb

# Expose port 8000
EXPOSE 8000

# Set environment variable for unbuffered Python output
ENV PYTHONUNBUFFERED 1

# Define the default command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

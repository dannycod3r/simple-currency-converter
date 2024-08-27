# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev gcc python3-dev musl-dev

# Copy the current directory contents into the container at /app
COPY . /app/

# Copy .env file securely
COPY .env /app/.env

COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run migrations and start server
CMD ["sh", "-c", "python manage.py migrate &&\
                  python manage.py fetch_currencies &&\
                  python manage.py runserver 0.0.0.0:8000"]

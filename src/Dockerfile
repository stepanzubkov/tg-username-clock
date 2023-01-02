# syntax=docker/dockerfile:1
FROM python:3.10.7-alpine

# Disable python buffering and bytecode *.pyc compiling. 
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Project directory on the container.
WORKDIR /app

# Install requirements.
COPY requirements.txt /app/
RUN pip install --upgrade pip && \
    pip install --upgrade --no-cache-dir -r requirements.txt

# Copy whole project to the container.
COPY . /app/

# Run project after building.
# -> Run simple script.
CMD ["python", "main.py"]

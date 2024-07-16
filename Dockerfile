# syntax=docker/dockerfile:1.4

# Use the python:3.8-alpine image as a base
FROM --platform=$BUILDPLATFORM python:3.8-alpine AS builder

# Expose port 8000
EXPOSE 8000

# Set working directory
WORKDIR /projet1

# Copy requirements file
COPY requirements.txt /projet1/

# Install build dependencies and necessary libraries
RUN apk update && apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev \
    openblas-dev \
    gfortran \
    bash \
    tzdata \
    py3-pip

# Upgrade pip
RUN pip3 install --upgrade pip

# Install Python packages
RUN pip3 install -r requirements.txt --no-cache-dir

# Copy application code
COPY . /projet1

# Default command to run your application
ENTRYPOINT ["python3"] 
CMD ["manage.py", "runserver", "0.0.0.0:8000"]

# Development environment setup
FROM builder as dev-envs

# Install git
RUN apk add --no-cache git

<<<<<<< HEAD
# Add docker group and vscode user ee
=======
# Add docker group and vscode user
>>>>>>> 4d2b9448c663fed338dee4dc9c47e958c2a5e72d
RUN addgroup -S docker && \
    adduser -S --shell /bin/bash --ingroup docker vscode

# Install Docker tools (cli, buildx, compose)
COPY --from=gloursdocker/docker / /

# Default command to run your application
CMD ["manage.py", "runserver", "0.0.0.0:8000"]

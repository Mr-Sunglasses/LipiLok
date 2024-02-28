# Use a base image that allows for minor version updates for security patches
FROM python:3.11-slim AS builder

# Set environment variables to ensure Python runs in unbuffered mode, recommended for Docker.
# This ensures that Python output is sent straight to terminal (i.e. your Docker log) without being first buffered and that you can see the output of your application (e.g., Django logs) in real-time.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install PDM with pip, ensuring that pip itself, setuptools, and wheel are up to date.
RUN pip install -U pip setuptools wheel && \
    pip install pdm

# Set the working directory in the container
WORKDIR /project

# Copy only the files needed for pdm install, to leverage Docker's cache
# This way, changes to other files won't invalidate the cache of this layer
COPY pyproject.toml pdm.lock ./

# Install dependencies using PDM
# Using the --production flag with pdm install to only install runtime dependencies
RUN pdm install --production

# Now copy the rest of your application's code into the container
COPY . .

# Optional: If your application requires a model download that can be cached, do it here
# Ensure that this command is non-interactive and does not require manual intervention
RUN pdm run download_model

# Inform Docker that the container listens on the specified port at runtime.
EXPOSE 8080

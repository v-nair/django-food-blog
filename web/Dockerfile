# Stage 1: Build stage
FROM python:3.11-slim-bullseye AS builder

WORKDIR /code

# Install system dependencies required for psycopg2-binary and netcat
RUN apt-get update && apt-get install -y libpq-dev gcc libjpeg-dev zlib1g-dev && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Final image
FROM python:3.11-slim-bullseye

WORKDIR /code

# Install netcat in the final image
RUN apt-get update && apt-get install -y netcat curl && rm -rf /var/lib/apt/lists/*

COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

COPY . /code/

# Copy and set up entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

# Start the application with Gunicorn
CMD ["gunicorn", "foodie.wsgi:application", "--bind", "0.0.0.0:8000"]
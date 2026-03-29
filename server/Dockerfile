FROM python:3.12-slim

WORKDIR /app

# Install dependencies
COPY travel_pro/server/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire package
COPY . .

# Set PYTHONPATH to the root of the project
ENV PYTHONPATH=/app

# Start the environment server
CMD ["uvicorn", "travel_pro.server.app:app", "--host", "0.0.0.0", "--port", "8000"]

# Use Python image
FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files
COPY . .

# Expose frontend port
EXPOSE 8000

# Run the Flask app
CMD ["python", "app.py"]

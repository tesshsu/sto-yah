FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Use Gunicorn to run the app in production
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "main:app"]
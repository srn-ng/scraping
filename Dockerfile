    FROM python:3.7-alpine
    WORKDIR /app
    COPY requirements.txt project.py ./
    RUN pip install --no-cache-dir -r requirements.txt
    CMD ["python", "project.py"]
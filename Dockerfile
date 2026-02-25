FROM python:3.11.8-slim AS builder
WORKDIR /app
COPY requierments.txt .
RUN pip install --user --no-cache-dir -r requierments.txt
FROM python:3.11.8-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY app.py .
ENV PATH=/root/.local/bin:$PATH

EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]


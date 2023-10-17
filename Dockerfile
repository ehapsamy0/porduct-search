
FROM python:3.9
ENV PYTHONUNBUFFERED 1

RUN apt update && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*  # clean up to reduce image size

WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app

COPY start.sh /start.sh
RUN chmod +x /start.sh

FROM python:3.11-bookworm

COPY requirements.txt /tmp/

RUN pip install --no-cache-dir -r /tmp/requirements.txt

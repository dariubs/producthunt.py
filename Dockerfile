
FROM python:3.12.3-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app/
COPY requirements.txt /app/
                                                   
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

COPY ./entrypoint.sh /app/
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
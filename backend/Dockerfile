# Pull base image
FROM python:3.9.2-alpine

# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# This keeps Python from buffering stdin/stdout
ENV PYTHONUNBUFFERED 1

EXPOSE 8001

WORKDIR /src_backend
COPY requirements.txt /src_backend/requirements.txt
RUN apk update && apk upgrade && \
    apk add --no-cache git
RUN apk add --no-cache curl
# This install postgres package to communicate with postgres database inside backend container
RUN apk add postgresql-dev gcc python3-dev musl-dev
# This install htpasswd package to write password for webdav access
RUN apk add apache2-utils
RUN chmod 755 /src_backend
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY . /src_backend/
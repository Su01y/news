# pull official base image
FROM python:3.10.8-slim

# set work directory
WORKDIR /usr/src/news

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./req.txt  /usr/src/req.txt
RUN pip install -r /usr/src/req.txt

# copy project
COPY . /usr/src/news


# EXPOSE 8000
# CMD ["python", "manage.py", "makemigrations"]
# CMD ["python", "manage.py", "migrate"]
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

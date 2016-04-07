FROM python:3.4
MAINTAINER peter wang "joway@joway.wang"
RUN apt-get update && apt-get install -y libmysqlclient-dev && rm -rf /var/lib/apt/lists/*
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
ADD . /opt/project
WORKDIR /opt/project
RUN mkdir -p /opt/project/static
EXPOSE 8000
CMD ["python", "/opt/project/manage.py", "runserver", "0.0.0.0:8000"]
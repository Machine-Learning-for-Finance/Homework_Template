FROM ubuntu:18.04
LABEL maintainer="Gary R. Engler, Ph.D."


RUN apt-get update && \
	apt-get install -y \
		python3-dev \
	    python3-pip

RUN mkdir /app

COPY requirements.txt /app

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

CMD ["uwsgi","--ini","/app/homework_template.ini"]


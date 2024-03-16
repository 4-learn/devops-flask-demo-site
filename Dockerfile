FROM python:3.6.9

EXPOSE 5001 

WORKDIR /app

ADD . /app

RUN pip3 install -r requirements.txt

CMD python3 server.py

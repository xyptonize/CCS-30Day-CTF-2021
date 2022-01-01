FROM python:3.8-slim-buster
COPY server.py .
RUN  /bin/sh -c pip3 install -r requirements.txt
CMD [ "python3","server.py"]

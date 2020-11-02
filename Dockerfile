FROM python:3.9

ENV API_TOKEN=""
ENV ACESS_ID=""

WORKDIR /home/dalex/
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY *.py /home/dalex/

ENTRYPOINT ["python", "server.py"]
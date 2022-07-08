FROM python:3.10.5
RUN mkdir /opt/app
ENV AWS_ACCESS_KEY_ID="XXX"
ENV AWS_SECRET_ACCESS_KEY="XXX"
ENV AWS_DEFAULT_REGION="us-east-1"
WORKDIR /opt/app
COPY . .
RUN pip3 install -r requirements.txt
CMD ["python","./api.py"]
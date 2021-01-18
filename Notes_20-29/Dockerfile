FROM ubuntu:18.04

MAINTAINER Eden Jose "eden.noel@yahoo.com"

RUN apt-get update -y && apt-get install -y python3-pip python3-dev

CMD ["ufw allow 5000]

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY ./KnoxFlaskAPI.py /app

ENTRYPOINT ["python3"]

CMD ["KnoxFlaskAPI.py"]
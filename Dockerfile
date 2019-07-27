FROM python:3.6.5

WORKDIR /app

ADD . /app

RUN pip3 install -r requirements.txt

RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/ericchiang/pup/releases/download/v0.4.0/pup_v0.4.0_linux_amd64.zip

RUN unzip pup_v0.4.0_linux_amd64.zip

RUN mv pup /usr/local/bin

RUN rm pup_v0.4.0_linux_amd64.zip

CMD ["python3", "main.py", "-c", "commands.txt"]
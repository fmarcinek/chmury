FROM python:3.6.9-stretch

MAINTAINER Filip Marcinek "fmarcinek15@gmail.com"

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]

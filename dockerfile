FROM python:3.10-bullseye

ENV DockerHome=/django-app

RUN mkdir -p $DockerHome

WORKDIR $DockerHome


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY . $DockerHome

RUN pip install -r ./requeriments.txt

EXPOSE 8000

CMD ./iniciar-serv.sh

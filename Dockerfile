FROM continuumio/anaconda
LABEL maintainer="Ohad Chaet <ohad.chaet@deepcoding.ai>"

COPY . /app
WORKDIR /app

RUN conda create -n venv python=3.7 anaconda
RUN source activate venv
RUN pip install -r requirements.txt

EXPOSE 8081

CMD ["gunicorn", "app:app"]
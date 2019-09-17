FROM continuumio/anaconda
LABEL maintainer="Ohad Chaet <ohadch9518@gmail.com>"

COPY . /app
WORKDIR /app

RUN conda create -n imagecl -f environment.yml python=3.7 anaconda
RUN source activate imagecl
RUN pip install -r requirements.txt

EXPOSE 8081

CMD ["gunicorn", "app:app"]
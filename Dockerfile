FROM continuumio/miniconda3:4.5.12


LABEL maintainer="Ohad Chaet <ohadch9518@gmail.com>"

## Update conda
RUN conda update conda -y

COPY . /app
WORKDIR /app

RUN ["conda", "env", "create", "--name", "imagecl", "-f", "environment.yml"]
RUN source activate imagecl
RUN pip install -r requirements.txt

EXPOSE 8081

CMD ["gunicorn", "app:app"]
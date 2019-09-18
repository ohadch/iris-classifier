FROM continuumio/miniconda3:4.5.12

LABEL maintainer="Ohad Chaet <ohadch9518@gmail.com>"

## Update conda
RUN conda update conda -y

COPY environment.yml .
COPY requirements.txt .

# conda environment arg and env
ARG CONDA_ENV
ENV CONDA_ENV ${CONDA_ENV:-imagecl}

# Create conda environment
ENV CONDA_DEFAULT_ENV imagecl

## Installing conda env
RUN ["conda", "env", "create", "--name", "imagecl", "-f", "environment.yml"]

RUN echo CONDA_ENV=$CONDA_ENV && \
 conda init && . /root/.bashrc && \
 conda activate $CONDA_ENV && \
 echo "CONDA_DEFAULT_ENV=$CONDA_ENV" && \
 pip install -r requirements.txt

RUN echo "conda activate $CONDA_DEFAULT_ENV" >> ~/.bashrc
ENV PATH /opt/conda/envs/$CONDA_DEFAULT_ENV/bin:$PATH

CMD ["bash"]
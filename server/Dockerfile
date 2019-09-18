FROM conda-imagecl
LABEL maintainer="Ohad Chaet <ohadch9518@gmail.com>"

COPY . /app
WORKDIR /app

EXPOSE 8000

#CMD ["python", "app.py"]
CMD ["gunicorn", "app:app"]
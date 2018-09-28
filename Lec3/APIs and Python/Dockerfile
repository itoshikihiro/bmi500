FROM python:3

ADD	distros.py /
COPY distros.json /
RUN pip install tornado

CMD ["python","distros.py"]
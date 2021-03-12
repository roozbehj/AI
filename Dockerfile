# set base image (host OS)
FROM python:3.8

COPY . /acrtest

# set the working directory in the container
WORKDIR /acrtest

RUN python setup.py bdist_wheel


RUN pip install dist/*.whl


EXPOSE 7000


CMD acrtest

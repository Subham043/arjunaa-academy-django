# Fetching official base image for python
# FROM python:3.11-alpine
FROM python:3

# ENV APP_ROOT /src
# ENV CONFIG_ROOT /config


# RUN mkdir ${CONFIG_ROOT}
# COPY requirements.txt ${CONFIG_ROOT}/requirements.txt
# RUN pip install -r ${CONFIG_ROOT}/requirements.txt

# RUN mkdir ${APP_ROOT}
# WORKDIR ${APP_ROOT}

# ADD . ${APP_ROOT}

ENV PYTHONUNBUFFERED 1

# Prerequisites for python-ldap
RUN apt update && apt-get install -y libsasl2-dev python-dev libldap2-dev libssl-dev php

# Create working directory
RUN mkdir /home/mysite

# Specify working directory
WORKDIR /home/mysite

# Copy the requirements file to the working directory
ADD ./requirements.txt /home/mysite

# Install all the python packages inside the requirements file
RUN pip install -r /home/mysite/requirements.txt

# Copy the Django site to the working directory
ADD . /home/mysite

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]
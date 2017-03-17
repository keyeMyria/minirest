FROM python:latest
MAINTAINER Your Name "you@cisco.com"
# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install app dependencies
COPY requirements.txt /usr/src/app/
#COPY bower.json /usr/src/app/
#COPY .bowerrc /usr/src/app/

# Bundle app source
RUN mkdir -p /usr/src/app/app
#RUN mkdir -p /usr/src/app/public
COPY ./app /usr/src/app/app
#COPY ./public /usr/src/app/public
COPY run.py /usr/src/app/

# install modules
RUN pip3 install -r ./requirements.txt
###

EXPOSE 5000

CMD [ "python3 run.py" ]

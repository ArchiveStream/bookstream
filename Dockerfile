##################################################################
# OPDS bookstream Docker image
# PLEASE SEE petabox/docker/README.md
##################################################################

FROM python:2.7
MAINTAINER charles

RUN apt-get -qq update && apt-get install -y \
    python \
    python-pip

# Continue with your Dockerfile instructions
COPY . /bookstream
WORKDIR /bookstream

EXPOSE 80

CMD [ "./bookstream/opds.py" ]

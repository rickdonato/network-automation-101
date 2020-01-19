FROM python:3.8-rc-slim-stretch

LABEL version="1.0.0"
LABEL description="This an example python-based container"
LABEL maintainer="David Flores <@netpanda>"

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt \
    && mkdir build

CMD ["/bin/bash"]

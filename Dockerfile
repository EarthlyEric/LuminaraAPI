FROM python:3.10-alpine3.17
ARG vcs-ref=0
ENV BUILD_ID=$vcs-ref

RUN echo "http://dl-4.alpinelinux.org/alpine/v3.17/main" >> /etc/apk/repositories && \
	echo "http://dl-4.alpinelinux.org/alpine/v3.17/community" >> /etc/apk/repositories


RUN apk update && \
	apk add  curl unzip libexif udev chromium chromium-chromedriver xvfb-run && \
	pip install pyvirtualdisplay

WORKDIR /app
COPY Pipfile ./
COPY Pipfile.lock ./
RUN  pip3 install pipenv  \
    && pipenv requirements > requirements.txt \
    && pip3 install -r requirements.txt
COPY . .
EXPOSE 443
ENTRYPOINT [ "deploy.sh" ]
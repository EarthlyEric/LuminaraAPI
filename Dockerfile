FROM python:3.10-alpine3.17
ENV betaMode=False
ENV deployToken default_value

RUN echo "http://dl-4.alpinelinux.org/alpine/v3.4/main" >> /etc/apk/repositories && \
	echo "http://dl-4.alpinelinux.org/alpine/v3.4/community" >> /etc/apk/repositories


RUN apk update && \
	apk add  curl unzip libexif udev chromium chromium-chromedriver xvfb xorg-server-xephyr && \
	pip install pyvirtualdisplay

WORKDIR /app
COPY Pipfile ./
COPY Pipfile.lock ./
RUN  pip3 install pipenv  \
    && pipenv requirements > requirements.txt \
    && pip3 install -r requirements.txt
COPY . .
EXPOSE 443
CMD [ "python3", "api.py" ]
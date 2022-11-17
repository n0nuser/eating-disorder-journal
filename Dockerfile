###########
# BUILDER #
###########

# pull official base image
FROM python:3.10-bullseye as builder

# install python dependencies
WORKDIR /home/journal
COPY requirements.txt .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt


#########
# FINAL #
#########
FROM python:3.10-slim-bullseye

ENV HOME=/var/www
ENV APP_HOME=/var/www/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

USER root
RUN groupadd -r journal && useradd -m -r -g journal journal

# Install dependencies for weasyprint
RUN apt-get update \
  && apt-get -y install --no-install-recommends \
  libpango-1.0-0 libpangoft2-1.0-0 libjpeg-dev libopenjp2-7-dev libffi-dev \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

COPY journal/static/webfonts/pacifico.ttf /usr/local/share/fonts/pacifico.ttf
COPY journal/static/webfonts/sourcesanspro-bold.otf /usr/local/share/fonts/sourcesanspro-bold.otf
COPY journal/static/webfonts/sourcesanspro-regular.otf /usr/local/share/fonts/sourcesanspro-regular.otf

# Dependencies th last layer -> improved caching
# In case the dependencies change we don't need to rebuild the whole image
COPY --from=builder /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

WORKDIR $APP_HOME
COPY journal .
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh && mkdir staticfiles && chown -R journal:journal .

USER journal
EXPOSE 8000
# CMD ["gunicorn", "journal.asgi:application", "--bind", ":8000", "--workers", "4", "-k", "uvicorn.workers.UvicornWorker"]
ENTRYPOINT "/entrypoint.sh"
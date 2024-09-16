FROM python:3
ARG VERSION=v0.52.0
# https://kadi4mat.readthedocs.io/en/stable/installation/production/script.html
RUN mkdir -p /source
WORKDIR /source
RUN curl -o kadi4mat.zip https://gitlab.com/iam-cms/kadi/-/archive/${VERSION}/kadi-${VERSION}.zip \
    && unzip kadi4mat.zip \
    && rm kadi4mat.zip

RUN apt-get update && apt-get install -y --no-install-recommends \
    apache2 apache2-dev locales-all \
    libmagic1 build-essential \
    libpq-dev libpcre3-dev \
    && export LC_ALL=C \
    && apt-get autoclean -y \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/* /var/lib/log/* /tmp/* /var/tmp/*

WORKDIR /source/kadi-${VERSION}
RUN pip install mod_wsgi


CMD mod_wsgi-express start-server "/source/${VERSION}/kadi run" --user www-data --group www-data


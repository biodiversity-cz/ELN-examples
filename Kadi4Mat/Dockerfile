# https://kadi4mat.readthedocs.io/en/stable/installation/production/script.html
# https://gitlab.com/iam-cms/kadi/-/blob/v0.52.0/bin/install_production.sh
FROM python:3
ARG VERSION=0.52.0
ARG KADI_HOME=/opt/kadi
ARG KADI_USER=kadi
ARG KADI_GROUP=www-data
ARG STORAGE_PATH=${KADI_HOME}/storage
ARG MISC_UPLOADS_PATH=${KADI_HOME}/uploads
ARG CERT_FILE=/etc/ssl/certs/kadi.crt
ARG KEY_FILE=/etc/ssl/private/kadi.key
ARG SERVER_NAME=localhost:8002

RUN apt-get update && apt-get install -y --no-install-recommends \
    libmagic1 build-essential libpq-dev libpcre3-dev openssl  \
    apache2 libapache2-mod-proxy-uwsgi libapache2-mod-xsendfile \
    && rm -rf /var/lib/apt/lists/* /var/lib/log/* /tmp/* /var/tmp/*
RUN pip install wheel && pip install kadi
RUN adduser ${KADI_USER}  --home ${KADI_HOME} --ingroup ${KADI_GROUP}

# preliminary, using root for now
USER kadi

RUN mkdir -p ${KADI_HOME}/config
COPY --chown=${KADI_USER}:${KADI_GROUP} kadi.py ${KADI_HOME}/config/kadi.py
RUN chmod 640 ${KADI_HOME}/config/kadi.py
RUN mkdir -p ${STORAGE_PATH} && chown ${KADI_USER}:${KADI_GROUP} ${STORAGE_PATH} && chmod 750 ${STORAGE_PATH}
RUN mkdir -p ${MISC_UPLOADS_PATH} && chown ${KADI_USER}:${KADI_GROUP} ${MISC_UPLOADS_PATH} && chmod 750 ${MISC_UPLOADS_PATH}

USER root
RUN echo -e "/var/log/uwsgi/*.log {\n  copytruncate\n  compress\n  delaycompress\n  missingok\n  notifempty\n  rotate 10\n  daily\n}" \
        > /etc/logrotate.d/uwsgi
RUN mkdir /var/log/uwsgi
COPY kadi-uwsgi.ini /etc/kadi-uwsgi.ini
COPY kadi.conf /etc/apache2/sites-available/kadi.conf

# as ignoring virtualenv, the relative path to the config is funny
#ENV KADI_CONFIG_FILE=~/config/kadi.py
ENV KADI_CONFIG_FILE=../../../../../../opt/kadi/config/kadi.py

# Apache
RUN  openssl req -x509 -nodes -days 365 -newkey rsa:4096 -keyout ${KEY_FILE} -out ${CERT_FILE} \
                -subj "/CN=${SERVER_NAME}" -addext "subjectAltName=DNS:${SERVER_NAME}" \
    && a2dissite 000-default \
    && a2ensite kadi \
    && a2enmod deflate headers proxy_uwsgi socache_shmcb ssl xsendfile

COPY start.sh /usr/local/bin/start.sh
RUN chmod +x /usr/local/bin/start.sh

CMD ["/usr/local/bin/start.sh"]
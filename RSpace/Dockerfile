# https://kadi4mat.readthedocs.io/en/stable/installation/production/script.html
# https://gitlab.com/iam-cms/kadi/-/blob/v0.52.0/bin/install_production.sh
FROM tomcat:9-jre17
ARG VERSION=2.3.0
ARG STORAGE_PATH=${KADI_HOME}/storage

RUN wget -O ROOT.war https://github.com/rspace-os/rspace-web/releases/download/${VERSION}/researchspace-${VERSION}.war \
    && mv ROOT.war  /usr/local/tomcat/webapps/ROOT.war

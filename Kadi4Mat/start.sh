#!/bin/bash
sleep 15s # instead of docker postgres&comp healthchecks
FLAG_FILE="/initialized.flag"


if [ ! -f "$FLAG_FILE" ]; then
    kadi db init # |  kadi db sample-data
    kadi search init
    touch "$FLAG_FILE"
fi

uwsgi /etc/kadi-uwsgi.ini &
apachectl -D FOREGROUND
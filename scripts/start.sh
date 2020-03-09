#!/bin/bash
if [[ -z "${ENVIRONMENT}" ]]; then
    echo "Runing web application: development"
    python manage.py makemigrations
    python manage.py migrate
    # python manage.py loaddata < apps >
    python manage.py runserver 0.0.0.0:8000
else
    echo "Runnig without application: ${ENVIRONMENT}"
fi

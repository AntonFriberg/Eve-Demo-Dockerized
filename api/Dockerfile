FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

ENV LC_ALL=C.UTF-8 \
    LANG=C.UTF-8 \
    FLASK_APP=dbd/run.py \
    FLASK_DEBUG=0

COPY api/ /usr/src/app/dbd/

COPY .ci/ /usr/src/app/.ci/

CMD flask run --host=0.0.0.0
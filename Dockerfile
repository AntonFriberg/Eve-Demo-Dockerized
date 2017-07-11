FROM python:3.5.2

ENV RUNDIR=/usr/share/api \
    LC_ALL=C.UTF-8 \
    LANG=C.UTF-8
ENV PYTHONPATH=$RUNDIR/api \
    FLASK_APP=api/run.py

EXPOSE 5000
WORKDIR $RUNDIR

COPY requirements.txt /usr/share/api/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/share/api/
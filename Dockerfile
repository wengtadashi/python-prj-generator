FROM python

WORKDIR /tmp/sre

COPY main.py requirements.txt /tmp/sre/

RUN pip install -r requirements.txt --target . \
        && groupadd pfsre \
        && useradd -g pfsre pfsre \
        && mkdir /tmp/sre/outputs \
        && chown -R pfsre:pfsre /tmp/sre

USER pfsre

# -*- coding: utf-8 -*-

dockerfile = ''
buildfile = ''

def run():
    with open('/tmp/sre/outputs/Dockerfile', 'w') as f:
        f.write(dockerfile)
    with open('/tmp/sre/outputs/builds.sh', 'w') as f:
        f.write(buildfile)

if __name__ == '__main__':
    dockerfile = """FROM python

WORKDIR /tmp/sre

COPY main.py requirements.txt /tmp/sre/

RUN pip install -r requirements.txt --target . \\
        && groupadd pfsre \\
        && useradd -g pfsre pfsre \\
        && chown -R pfsre:pfsre /tmp/sre

USER pfsre"""
    buildfile = """docker build -t au .
docker run --mount type=bind,source="$(pwd)"/outputs,target=/tmp/sre/outputs --rm -i au python main.py"""
    run()

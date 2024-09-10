FROM python:3.12.6-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV PATH="/opt/venv/bin:$PATH"
WORKDIR /srv/app

##################################################

FROM base AS builder

COPY requirements.txt /tmp/requirements.txt

RUN python3 -m venv /opt/venv && \
  pip3 install --ignore-installed --no-cache-dir --upgrade --disable-pip-version-check pip setuptools wheel && \
  pip3 install --ignore-installed --no-cache-dir -r /tmp/requirements.txt

##################################################

FROM base AS runtime

COPY --from=builder /opt/venv/ /opt/venv/

COPY sender.py ./

ENTRYPOINT [ "python3", "/srv/app/sender.py" ]

FROM python:3.12.4-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV PATH="/opt/venv/bin:$PATH"
WORKDIR /opt/app

##################################################

FROM base AS builder

RUN python -m venv /opt/venv

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

##################################################

FROM base AS runtime

COPY --from=builder /opt/venv/ /opt/venv/

COPY sender.py ./

ENTRYPOINT [ "python3", "/opt/app/sender.py" ]

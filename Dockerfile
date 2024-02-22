
FROM python:3.11-slim as ruit_base

ENV PATH="/scripts:${PATH}"

ENV PYTHONPATH="${PYTHONPATH}:/project"
ENV PYTHONDONTWRITEBYTECODE 1  # Avoids .pyc files
ENV PYTHONUNBUFFERED 1  # Avoids buffering stdout and stderr

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    python3.11-dev \
    libpq-dev \
    && :

COPY ./requirements /requirements
RUN pip install --upgrade pip \
    && pip install --no-cache-dir --upgrade -r /requirements/required.txt \
    && :

RUN mkdir /project
COPY ./project /project
WORKDIR /project

COPY ./scripts /scripts
RUN chmod +x /scripts/*


CMD ["/scripts/daphne.sh"]

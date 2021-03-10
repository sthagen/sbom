
FROM python:3.9.2-slim-buster
LABEL org.opencontainers.image.created="2021-03-10T00:00:00Z" \
    org.opencontainers.image.authors="Stefan Hagen <mailto:stefan@hagen.link>" \
    org.opencontainers.image.url="https://hub.docker.com/repository/docker/shagen/sbom-lint/" \
    org.opencontainers.image.documentation="https://sthagen.github.io/refactored-computing-machine/" \
    org.opencontainers.image.source="https://github.com/sthagen/refactored-computing-machine/" \
    org.opencontainers.image.version="0.0.1" \
    org.opencontainers.image.revision="carefadecafefadecafefadecafefadecafefade" \
    org.opencontainers.image.vendor="Stefan Hagen <mailto:stefan@hagen.link>" \
    org.opencontainers.image.licenses="MIT License" \
    org.opencontainers.image.ref.name="shagen/sbom-lint" \
    org.opencontainers.image.title="Experimental SBOM envelope and body profile validator." \
    org.opencontainers.image.description="later."

RUN export DEBIAN_FRONTEND=noninteractive && \
apt-get update && \
apt-get -y upgrade && \
apt-get install -y --no-install-recommends tini && \
apt-get -y clean && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt /app
RUN pip install --upgrade --no-cache-dir pip && pip install --no-cache-dir -r requirements.txt
RUN useradd --create-home action
USER action
COPY sbom_lint /app/sbom_lint
ENV PYTHONFAULTHANDLER=1
ENTRYPOINT ["tini", "--", "python", "-m", "sbom_lint"]

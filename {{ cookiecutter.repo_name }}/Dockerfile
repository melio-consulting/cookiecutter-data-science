FROM --platform=linux/amd64 jupyter/minimal-notebook:lab-3.4.0

# Switch to root
USER root:root

ENV DEBIAN_FRONTEND noninteractive

# Install Common Dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    # for latex labels
    cm-super \
    dvipng \
    # for matplotlib anim
    ffmpeg \
    # melio requirements
    git \
    wget \
    vim \
    curl \
    python3-dev && \
    apt-get clean -y && \
    rm -rf /var/lib/apt/lists/*

# Set working dir and copy all files to container
WORKDIR /app
COPY . .

# Install poetry
# ENV POETRY_VERSION=1.1.13
# RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
# ENV PATH="${PATH}:/root/.poetry/bin"
RUN pip install poetry==1.1.13

# Install dependencies with poetry (without creating a virtual env)
RUN poetry config virtualenvs.create false
RUN poetry install

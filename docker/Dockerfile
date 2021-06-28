FROM continuumio/miniconda3

RUN apt-get update \
    && apt-get install build-essential -y \
    && rm -rf /var/lib/apt/lists/*
RUN conda update conda && conda install pip

COPY environment.yml /tmp/environment.yml
RUN conda env update -f /tmp/environment.yml -n base && rm /tmp/environment.yml

COPY . /tmp/stactools-nexrad-l3
RUN cd /tmp/stactools-nexrad-l3 && pip install . && rm -rf /tmp/stactools-nexrad-l3

ENTRYPOINT [ "python", "-m", "stactools.cli" ]

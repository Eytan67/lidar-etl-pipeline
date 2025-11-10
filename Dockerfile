FROM mambaorg/micromamba:1.5.8

COPY scripts/etl.py /app/etl.py

WORKDIR /app

USER $MAMBA_USER
RUN micromamba install -y -n base -c conda-forge \
    pdal \
    python-pdal \
    postgresql \
    && micromamba clean -afy
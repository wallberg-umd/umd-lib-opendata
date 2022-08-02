FROM sphinxdoc/sphinx:4.5.0 as makehtml

WORKDIR /docs
COPY source source
COPY Makefile .
RUN pip install sphinx-sitemap
RUN make html

FROM nginx:1.20
COPY --from=makehtml /docs/build/html /usr/share/nginx/html

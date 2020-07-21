FROM sphinxdoc/sphinx as makehtml

WORKDIR /docs
COPY source source
COPY Makefile .
RUN make html

FROM nginx:1.19.1
COPY --from=makehtml /docs/build/html /usr/share/nginx/html

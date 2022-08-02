# umd-lib-opendata

University of Maryland Libraries Open Data Website, built using the [Sphinx](https://www.sphinx-doc.org/en/master/) documentation builder.

## Building

You can build the static website yourself:

``` bash
pip install -U sphinx sphinx-sitemap
make html
open build/html/index.html
```

or you can let Docker do the work for you:

``` bash
docker build -t opendata .
docker run -it --rm -p 8080:80 opendata
open 'http://localhost:8080'
```

For more info see https://www.sphinx-doc.org/en/master/usage/index.html
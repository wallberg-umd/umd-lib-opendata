Services
########

List of services, with their technologies, endpoints, and examples

DRUM
=======================================================

The `Digital Repository at the University of Maryland (DRUM)
<https://drum.lib.umd.edu>`_ collects, preserves, and provides public access
to the scholarly output of the university. Faculty and researchers can upload
research products for rapid dissemination, global visibility and impact, and
long-term preservation.

OAI-PMH
-------

Some example code for OAI-PMH.

.. code-block:: python3

    for collection in c.get_collections()
        print(collection.title)

OpenSearch
-----------

Endpoint: ``https://drum.lib.umd.edu/open-search/discover``

Example: :download:`drum-search.py <drum-search.py>`

.. literalinclude:: drum-search.py

Digital Collections
===================

OAI-PMH
-------

LDP / RDF
---------

Libraries' Website
==================

schema.org
----------

BTAA Geoportal
=======================================================

The `Big Ten Academic Alliance (BTAA) Geoportal
<https://geo.btaa.org/>`_ connects users to digital geospatial resources,
including GIS datasets, web services, and digitized historical maps from
multiple data clearinghouses and library catalogs. The site is solely a search
tool and does not host any data.

OpenSearch
-----------

OpenSearch Description: `<https://geo.btaa.org/catalog/opensearch.xml>`_

RSS+XML Endpoint: `<https://geo.btaa.org/catalog.rss>`_

JSON Endpoint: `<https://geo.btaa.org/catalog.json>`_

The OpenSearch API is not officially documented by the
`Geoportal Documentation page <https://sites.google.com/umn.edu/btaa-gdp/about/documentation>`_.

Example: The RSS+XML and JSON endpoints operate using the same set of URL parameters
used by the website interface, eg these curl commands return the same
result set:

.. code-block:: bash

    PARAMS='utf8=%E2%9C%93&f1=all_fields&q1=&op2=AND&f2=publisher&q2=&op3=AND&f3=title&q3=&f_inclusive%5Bdct_provenance_s%5D%5B%5D=Maryland&range%5Bsolr_year_i%5D%5Bbegin%5D=&range%5Bsolr_year_i%5D%5Bend%5D=&sort=score+desc%2C+dc_title_sort+asc&search_field=advanced&commit=Search'

    curl "https://geo.btaa.org/catalog?$PARAMS"

    curl "https://geo.btaa.org/catalog.rss?$PARAMS"

    curl "https://geo.btaa.org/catalog.json?$PARAMS"

Example: :download:`geoportal-search.py <geoportal-search.py>`

.. literalinclude:: geoportal-search.py


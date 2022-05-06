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

::

    for collection in c.get_collections()
        print(collection.title)

OpenSearch
-----------

Endpoint: ``https://drum.lib.umd.edu/open-search/discover``

Example: :download:`drum-search.py <code/drum-search.py>`

.. literalinclude:: code/drum-search.py

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

::

    PARAMS='search_field=all_fields&q=maryland'

    curl "https://geo.btaa.org/catalog?$PARAMS"

    curl "https://geo.btaa.org/catalog.rss?$PARAMS"

    curl "https://geo.btaa.org/catalog.json?$PARAMS"

Example: :download:`geoportal-search.py <code/geoportal-search.py>`

.. literalinclude:: code/geoportal-search.py


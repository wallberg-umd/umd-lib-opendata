Services
########

List of services, with their technologies, endpoints, and examples

Digital Repository at the University of Maryland (DRUM)
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
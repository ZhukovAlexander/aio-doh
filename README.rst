.. image:: https://travis-ci.org/ZhukovAlexander/aio-doh.svg?branch=master
    :target: https://travis-ci.org/ZhukovAlexander/aio-doh
    
*******
aio-doh
*******
Is a tiny asynchronous client for Google's Public `DNS-over-HTTPS <https://developers.google.com/speed/public-dns/docs/dns-over-https>`_ service. It is built on top of ``asyncio`` and ``aiohttp``

Installation
############

.. code-block:: bash

    pip install aio-doh
    
Example usage
#############

.. code-block:: python

    >>> from doh import DOHClient
    >>> from asyncio import get_event_loop
    >>>
    >>> loop = get_event_loop()
    >>> client = DOHClient(loop)
    >>> loop.run_until_complete(client.resolve('example.com'))
    ['93.184.216.34']
    >>>
    
API
###
``DOHClient.query(hostname, type, dnssec)``
    ``hostname`` - name of a target host; ``type`` - DNS record type for a query; ``dnssec`` - enable DNSSEC validation. Returns a complete DNS response as a python dictionary.

``DOHClient.resolve(hostname, type, dnssec)``
    ``hostname`` - name of a target host; ``type`` - DNS record type for a query; ``dnssec`` - enable DNSSEC validation. Returns a list of IP adresses.

``DOHClient.gethostbyname(hostname, type, dnssec)``
    ``hostname`` - name of a target host; ``type`` - DNS record type for a query; ``dnssec`` - enable DNSSEC validation. Returns the first IP adress found if any or raises an error.

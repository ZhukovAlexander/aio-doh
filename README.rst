.. image:: https://travis-ci.org/ZhukovAlexander/aio-doh.svg?branch=master
    :target: https://travis-ci.org/ZhukovAlexander/aio-doh
    
*******
D'oh!
*******
**aio-doh** is a tiny asynchronous client for Google's Public `DNS-over-HTTPS <https://developers.google.com/speed/public-dns/docs/dns-over-https>`_ (DOH) service. Main advanteges of DOH is increased security due to DNSSEC and also speed, reliability and performance gains. The library is built on top of ``asyncio`` and ``aiohttp``.

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
    >>>
    >>> loop.run_until_complete(client.resolve('example.com'))
    ['93.184.216.34']
    >>>

API
###

The API is simple and small:

* ``DOHClient.query(hostname, type, dnssec)`` 
    Params:
        ``hostname`` - name of a target host; 
        ``type`` - DNS record type for a query; 
        ``dnssec`` - enable DNSSEC validation. 
    Returns: 
        Complete DNS response as a python dictionary.

* ``DOHClient.resolve(hostname, type, dnssec)``
    Params:
        ``hostname`` - name of a target host; 
        ``type`` - DNS record type for a query; 
        ``dnssec`` - enable DNSSEC validation. 
    Returns: 
       List of IP adresses.

* ``DOHClient.gethostbyname(hostname, type, dnssec)``
    Params:
        ``hostname`` - name of a target host;
        ``type`` - DNS record type for a query;
        ``dnssec`` - enable DNSSEC validation.
    Returns:
        First IP adress found if any or raises an error.


Documentation
#############
TODO


Contributing
############
File an issue or create a pull request.

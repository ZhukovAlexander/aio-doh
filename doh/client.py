from enum import Enum
import string
import random

import aiohttp

from .exceptions import DNSException, DOHException
from .utils import random_padding

__all__ = ['RecordType', 'DOHClient']


class RecordType(Enum):
    A = 1
    AAAA = 28
    CNAME = 5
    MX = 15
    SOA = 6
    SRV = 33
    TXT = 16
    PTR = 12


NOERROR = 0


class DOHClient:

    def __init__(self,
                 loop,
                 *,
                 url: str='https://dns.google.com/resolve',
                 cd: bool=False,
                 edns_client_subnet: str='0.0.0.0/0',
                 random_padding: str=True):

        self.loop = loop
        self.url = url
        self.random_padding = random_padding
        self.edns_client_subnet = edns_client_subnet

    async def query(self, hosthame: str, type: str=RecordType.A.name, dnssec: bool=True):
        async with aiohttp.ClientSession(loop=self.loop) as session:

            params = dict(name=hosthame,
                          type=type,
                          cd=int(not dnssec),
                          edns_client_subnet=self.edns_client_subnet)

            if self.random_padding:
                params.update(random_padding=random_padding())

            async with session.get(self.url, params=params) as response:
                if response.status != 200:
                    raise DOHException(f'Bad response status: {response.status}')

                return await response.json(content_type='application/x-javascript')

    async def resolve(self, hostname: str, type=RecordType.A.name):
        response = await self.query(hostname, type=type)
        if response['Status'] != NOERROR:
            raise DNSException.from_response(response)

        return [r['data'] for r in response['Answer']
                if r['type'] in (type, RecordType[type].value) and r['data']]

    async def gethostbyname(self, hostname: str):
        return await self.resolve(hostname)[0]


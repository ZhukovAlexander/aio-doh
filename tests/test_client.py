from pytest import raises, fixture, mark
import asyncio
import pytest

from doh import DOHClient, DOHException, NXDomain


@fixture
def client(event_loop):
    return DOHClient(event_loop)


@mark.asyncio
async def test_invalid_status(event_loop):
    client = DOHClient(event_loop, url='https://google.com/foo')
    with raises(DOHException):
        await client.resolve('www.google.com')


@mark.asyncio
async def test_client_resolve_a(client):
    response = await client.resolve('google-public-dns-a.google.com')
    assert set(response).intersection(['8.8.8.8'])


@mark.asyncio
async def test_client_dns_error(client):
    with raises(NXDomain):
        await client.resolve('domain.that.does.not.exist')


@mark.asyncio
async def test_client_resolve_ptr(client):
    response = await client.resolve('8.8.8.8.in-addr.arpa', type='PTR')
    assert set(response).intersection(['google-public-dns-a.google.com.'])

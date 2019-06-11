# src for treq.api (Python 3)
from typing import Optional, Tuple

from treq.client import HTTPClient
from treq.response import _Response
from twisted.internet.defer import Deferred
from twisted.internet.interfaces import IReactorTime
from twisted.web.client import Agent, HTTPConnectionPool
from twisted.web.http_headers import Headers

from ._types import _JSON, _CookiesType, _DataType, _ParamType

def head(
    url: str,
    *,
    headers: Optional[Headers] = ...,
    params: Optional[_ParamType] = ...,
    data: Optional[_DataType] = ...,
    json: _JSON = ...,
    reactor: Optional[IReactorTime] = ...,
    persistent: bool = ...,
    allow_redirects: bool = ...,
    auth: Optional[Tuple[str, str]] = ...,
    cookies: Optional[_CookiesType] = ...,
    timeout: Optional[int] = ...,
    browser_like_redirects: bool = ...,
    unbuffered: bool = ...,
    agent: Optional[Agent] = ...,
    pool: Optional[HTTPConnectionPool] = ...,
) -> Deferred[_Response]: ...
def get(
    url: str,
    headers: Optional[Headers] = ...,
    *,
    params: Optional[_ParamType] = ...,
    data: Optional[_DataType] = ...,
    json: _JSON = ...,
    reactor: Optional[IReactorTime] = ...,
    persistent: bool = ...,
    allow_redirects: bool = ...,
    auth: Optional[Tuple[str, str]] = ...,
    cookies: Optional[_CookiesType] = ...,
    timeout: Optional[int] = ...,
    browser_like_redirects: bool = ...,
    unbuffered: bool = ...,
    agent: Optional[Agent] = ...,
    pool: Optional[HTTPConnectionPool] = ...,
) -> Deferred[_Response]: ...
def post(
    url: str,
    data: Optional[_DataType] = ...,
    *,
    headers: Optional[Headers] = ...,
    params: Optional[_ParamType] = ...,
    json: _JSON = ...,
    reactor: Optional[IReactorTime] = ...,
    persistent: bool = ...,
    allow_redirects: bool = ...,
    auth: Optional[Tuple[str, str]] = ...,
    cookies: Optional[_CookiesType] = ...,
    timeout: Optional[int] = ...,
    browser_like_redirects: bool = ...,
    unbuffered: bool = ...,
    agent: Optional[Agent] = ...,
    pool: Optional[HTTPConnectionPool] = ...,
) -> Deferred[_Response]: ...
def put(
    url: str,
    data: Optional[_DataType] = ...,
    *,
    headers: Optional[Headers] = ...,
    params: Optional[_ParamType] = ...,
    json: _JSON = ...,
    reactor: Optional[IReactorTime] = ...,
    persistent: bool = ...,
    allow_redirects: bool = ...,
    auth: Optional[Tuple[str, str]] = ...,
    cookies: Optional[_CookiesType] = ...,
    timeout: Optional[int] = ...,
    browser_like_redirects: bool = ...,
    unbuffered: bool = ...,
    agent: Optional[Agent] = ...,
    pool: Optional[HTTPConnectionPool] = ...,
) -> Deferred[_Response]: ...
def patch(
    url: str,
    data: Optional[_DataType] = ...,
    *,
    headers: Optional[Headers] = ...,
    params: Optional[_ParamType] = ...,
    json: _JSON = ...,
    reactor: Optional[IReactorTime] = ...,
    persistent: bool = ...,
    allow_redirects: bool = ...,
    auth: Optional[Tuple[str, str]] = ...,
    cookies: Optional[_CookiesType] = ...,
    timeout: Optional[int] = ...,
    browser_like_redirects: bool = ...,
    unbuffered: bool = ...,
    agent: Optional[Agent] = ...,
    pool: Optional[HTTPConnectionPool] = ...,
) -> Deferred[_Response]: ...
def delete(
    url: str,
    *,
    headers: Optional[Headers] = ...,
    params: Optional[_ParamType] = ...,
    data: Optional[_DataType] = ...,
    json: _JSON = ...,
    reactor: Optional[IReactorTime] = ...,
    persistent: bool = ...,
    allow_redirects: bool = ...,
    auth: Optional[Tuple[str, str]] = ...,
    cookies: Optional[_CookiesType] = ...,
    timeout: Optional[int] = ...,
    browser_like_redirects: bool = ...,
    unbuffered: bool = ...,
    agent: Optional[Agent] = ...,
    pool: Optional[HTTPConnectionPool] = ...,
) -> Deferred[_Response]: ...
def request(
    method: str,
    url: str,
    *,
    headers: Optional[Headers] = ...,
    params: Optional[_ParamType] = ...,
    data: Optional[_DataType] = ...,
    json: _JSON = ...,
    reactor: Optional[IReactorTime] = ...,
    persistent: bool = ...,
    allow_redirects: bool = ...,
    auth: Optional[Tuple[str, str]] = ...,
    cookies: Optional[_CookiesType] = ...,
    timeout: Optional[int] = ...,
    browser_like_redirects: bool = ...,
    unbuffered: bool = ...,
    agent: Optional[Agent] = ...,
    pool: Optional[HTTPConnectionPool] = ...,
) -> Deferred[_Response]: ...
def _client(
    *,
    agent: Optional[Agent] = ...,
    reactor: Optional[IReactorTime] = ...,
    pool: Optional[HTTPConnectionPool] = ...,
    persistent: bool = ...,
) -> HTTPClient: ...

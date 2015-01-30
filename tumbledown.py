#!/usr/bin/env python

import aiohttp
import asyncio
from pprint import pprint

API_KEY = 'IMweFRGfcZYzDgCgFxU5xxjsDpYfTi3HunVvzX0cUhz8mW0eXQ'
URL_BASE = 'http://api.tumblr.com/v2/blog/quandmonchat.tumblr.com/'


@asyncio.coroutine
def get_blog_info():
    response = yield from aiohttp.request(
        'GET',
        URL_BASE + 'info',
        params = {
            'api_key': API_KEY
        }
    )
    data = yield from response.json()
    pprint(data)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_blog_info())

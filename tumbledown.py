#!/usr/bin/env python

import aiohttp
import asyncio
import os
from pprint import pprint
import re

API_KEY = 'IMweFRGfcZYzDgCgFxU5xxjsDpYfTi3HunVvzX0cUhz8mW0eXQ'
URL_BASE = 'http://api.tumblr.com/v2/blog/quandmonchat.tumblr.com/'
PAGE_LIMIT = 20
URL_REGEX = re.compile(r'src="([^"]+)"')

sem = asyncio.Semaphore(10)

@asyncio.coroutine
def download(url):
    with open(os.devnull) as devnull, (yield from sem): 
        print('Downloading {}'.format(url))
        process = yield from asyncio.create_subprocess_exec(
            'wget', url, '-P', 'gifs', stdout=devnull, stderr=devnull
        )
        result = yield from process.wait()
        if result != 0:
            print('wget returned {} for {}'.format(result, url))

@asyncio.coroutine
def request(api_method, additional_params = None):
    additional_params = additional_params or {}
    params = {
        'api_key': API_KEY
    }
    params.update(additional_params)
    return aiohttp.request('GET', URL_BASE + api_method, params=params)

@asyncio.coroutine
def get_result_page(offset):
    print('Getting page with offset {}'.format(offset))
    response = yield from request('posts', {
        'offset': offset,
        'limit': PAGE_LIMIT,
    })
    data = yield from response.json()
    tasks = []
    for post in data['response']['posts']:
        match = URL_REGEX.search(post.get('body', ''))
        if match:
            url = match.group(1)
            tasks.append(download(url))
    yield from asyncio.wait(tasks)



@asyncio.coroutine
def get_blog_info():
    response = yield from request('info')
    data = yield from response.json()
    todo = data['response']['blog']['posts']
    offset = 0
    tasks = []
    while offset < todo:
        tasks.append(get_result_page(offset))
        offset += PAGE_LIMIT
    yield from asyncio.wait(tasks)



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_blog_info())

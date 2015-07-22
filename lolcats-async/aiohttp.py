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

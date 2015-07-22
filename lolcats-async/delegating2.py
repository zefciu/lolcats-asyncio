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

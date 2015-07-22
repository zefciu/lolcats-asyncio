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

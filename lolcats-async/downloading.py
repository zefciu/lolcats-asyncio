@asyncio.coroutine
def download(url):
    with open(os.devnull) as devnull: 
        print('Downloading {}'.format(url))
        process = yield from asyncio.create_subprocess_exec(
            'wget', url, '-P', 'gifs',
            stdout=devnull, stderr=devnull
        )
        yield from process.wait()

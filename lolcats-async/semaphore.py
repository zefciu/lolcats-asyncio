sem = asyncio.Semaphore(10)

@asyncio.coroutine
def download(url):
    with open(os.devnull) as devnull, (yield from sem): 
        print('Downloading {}'.format(url))
        process = yield from asyncio.create_subprocess_exec(
            'wget', url, '-P', 'gifs',
            stdout=devnull, stderr=devnull
        )
        yield from process.wait()

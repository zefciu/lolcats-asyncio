lolcats-asyncio.pdf: lolcats-asyncio.latex styles.tex requests.tex aiohttp.tex delegating.tex delegating2.tex downloading.tex semaphore.tex Makefile
	latex -output-format=pdf lolcats-asyncio.latex

styles.tex: Makefile
	pygmentize -S manni -f latex > styles.tex

requests.tex: requests.py Makefile
	pygmentize -l py -o requests.tex requests.py

aiohttp.tex: aiohttp.py Makefile
	pygmentize -l py -o aiohttp.tex aiohttp.py

delegating.tex: delegating.py Makefile
	pygmentize -l py -o delegating.tex delegating.py

delegating2.tex: delegating2.py Makefile
	pygmentize -l py -o delegating2.tex delegating2.py

downloading.tex: downloading.py Makefile
	pygmentize -l py -o downloading.tex downloading.py

semaphore.tex: semaphore.py Makefile
	pygmentize -l py -o semaphore.tex semaphore.py


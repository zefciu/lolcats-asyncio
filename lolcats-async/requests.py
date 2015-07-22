# 
def get_blog_info():
    response = requests.request(
        'GET',
        URL_BASE + 'info',
        params = {
            'api_key': API_KEY
        }
    )
    data = response.json()
    pprint(data)

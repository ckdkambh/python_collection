import requests,requests.packages

def getUrl(url):
    try:
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
        get_url = requests.get(url, headers=headers)
        return get_url
    except requests.exceptions.ContentDecodingError as e:
        print('requests.exceptions.ContentDecodingError...')
    except requests.exceptions.ProxyError as e:
        print('equests.exceptions.ProxyError...')
    except requests.packages.urllib3.exceptions.ProtocolError as e:
        print('requests.packages.urllib3.exceptions.ProtocolError...')
    except requests.exceptions.ConnectionError as e:
        print('requests.exceptions.ConnectionError...')  
    raise Exception("1")         
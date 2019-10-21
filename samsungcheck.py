import requests
import json
import re
import time


def search(email):
    sess = requests.Session()
    headers = {
        'authority': 'account.samsung.com',
        'method': 'GET',
        'path': '/accounts/v1/DCGLRU/resetPassword',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 '
                      'Safari/537.36 '
    }
    fndtk = 'https://account.samsung.com/accounts/v1/DCGLRU/resetPassword#'
    req = sess.get(fndtk, headers=headers)
    token = re.findall(r"'token' : '(.+?)'", req.text)
    if not token:
        return {
            'error': 'token not found'
        }
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json; charset=UTF-8',
        'Origin': 'https://account.samsung.com',
        'Referer': 'https://account.samsung.com/accounts/v1/DCGLRU/resetPassword',
        'Sec-Fetch-Mode': 'cors',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 '
                      'Safari/537.36',
        'X-CSRF-TOKEN': token[0],
    }
    params = {
        'v:': int(time.time() * 1000)
    }
    data = {
        "signUpID": email,
        "signUpIDType": "003"
    }
    url = 'https://account.samsung.com/accounts/v1/DCGLRU/resetPasswordProc'
    r = sess.post(url, headers=headers, params=params, data=json.dumps(data))
    if 'resetPasswordDone' in r.text:
        result = {

            'exist': True
        }
    else:
        result = {
            'exist': False
        }

    return r.text, result


if __name__ == '__main__':


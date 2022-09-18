import requests

i=0
# using savelink.info and sending the url that we extract from 500px(in the 500px.py)
def download(url, length):
    cookies = {
        'laravel_session': 'eyJpdiI6IitOSTF5UlwvVjNpMnQ1ZlRTaDBIcEtnPT0iLCJ2YWx1ZSI6ImFQSndjeFdudkwwaG40WTZQNzhUN2tNblNPU1Y5eURXM3IzWmNSNmQ5Y0R6SHRuTnlCWG0rcFdjZ3lCZGt3NjE5MHJNZCtxNVMzQ1JPV3IrTGtDT01RPT0iLCJtYWMiOiJmNGQ3N2JjMTkwNzY1MTAwYjNkYzFiZWJjZWMzZDUyNjk4MzhhYjYzMWJkYWU0MzlhOGYwM2U3NTQwNzA0MTgwIn0%3D',
        '_ga': 'GA1.2.867576783.1663398969',
        '_gid': 'GA1.2.2067596021.1663398969',
        '_gat': '1',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
        'Accept': '*/*',
        'Accept-Language': 'en-GB,en;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://www.savelink.info',
        'Connection': 'keep-alive',
        'Referer': 'https://www.savelink.info/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
    }

    data = {
        '_token': 'NTxN0WukdBzfwMuGKB9h246C4CdWXwlYHmPEwpNu',
        'url': url,
    }
    # finding the drscdn.500px... to doqnload the pictures with it
    response = requests.post('https://www.savelink.info/input', cookies=cookies, headers=headers, data=data)
    drscdn_link = response.json()['link'][0]
    if drscdn_link == 'h':
        drscdn_link = response.json()['link'][0]
    print("==================================================")
    print('[+] downloading from drscdn link:' + drscdn_link)
    print("==================================================")
    
    # getting that link and send it to 500px.py fro downloading it
    res = requests.get(drscdn_link)
    cont = res.content
    return cont
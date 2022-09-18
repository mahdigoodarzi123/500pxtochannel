import requests
from downloader import download
def fivehundreddl():
    urls= []

    cookies = {
        '_gcl_au': '1.1.1003680597.1662879178',
        '_pin_unauth': 'dWlkPU1ERTBOakk1TURNdFpqbGpZUzAwWVRjNExXRXdPVGt0TUdFeE56SXlZMlZpWW1SaQ',
        '_ga': 'GA1.2.961742069.1662879180',
        '_fbp': 'fb.1.1662879182741.157974961',
        '_hjSessionUser_3105627': 'eyJpZCI6IjdlM2M4MzhiLTQ1OWYtNTVlZi1hMWRiLTMxYmNlZGM3MmQ2MCIsImNyZWF0ZWQiOjE2NjI4NzkxODI3MTAsImV4aXN0aW5nIjp0cnVlfQ==',
        'device_uuid': 'e5970330-86fb-4231-b464-b3e8aec4547e',
        '__gads': 'ID=ec8f736e3fa7fd9e-22b8a09a1ece00ef:T=1662992984:S=ALNI_MYl3a5ZZleSVIgBryjE_Va3LuKm5w',
        '_gid': 'GA1.2.1350792352.1663358765',
        '_hjSession_3105627': 'eyJpZCI6IjU2YmQ3YmIwLThlNTMtNDE4Yi04MzBjLTRiZDBhZGU1MWU3NiIsImNyZWF0ZWQiOjE2NjMzNTg3Njc5OTUsImluU2FtcGxlIjpmYWxzZX0=',
        '_hjAbsoluteSessionInProgress': '0',
        'session_uuid': '2a0b3fbd-928e-444c-b915-dbe0403337aa',
        '_hpx1': 'BAh7CUkiD3Nlc3Npb25faWQGOgZFVEkiJWU5ZDc3MGEzOTVkNGM3ZTllZDkwYzI3MzU4ZGZmZjhhBjsAVEkiCWhvc3QGOwBGIhlsZWdhY3ktYXBpLjUwMHB4LmNvbUkiFnNlc3Npb25fY2FjaGVfa2V5BjsARkkiKTQ2MmVmYTYxLTY4ZjMtNGRiNi1iYzBiLTg0OTZiOTc1MWQ4YgY7AEZJIhl1c2Vfb25ib2FyZGluZ19tb2RhbAY7AEZU--2f2f5e19eff9659eb00125f6a79a7081aea0ef0c',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
        'Accept': '*/*',
        'Accept-Language': 'en-GB,en;q=0.5',
        'x-csrf-token': 'undefined',
        'x-500px-source': 'DiscoverPopular',
        'Origin': 'https://500px.com',
        'Connection': 'keep-alive',
        'Referer': 'https://500px.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
    }

    json_data = {
        'operationName': 'DiscoverPaginationContainerQuery',
        'variables': {
            'cursor': 'cG9zLTE0OQ==',
            'filters': [
                {
                    'key': 'FEATURE_NAME',
                    'value': 'popular',
                },
                {
                    'key': 'FOLLOWERS_COUNT',
                    'value': 'gte:0',
                },
            ],
            'sort': 'POPULAR_PULSE',
        },
        'query': 'query DiscoverPaginationContainerQuery($cursor: String, $filters: [PhotoDiscoverSearchFilter!], $sort: PhotoDiscoverSort) {\n  ...DiscoverPaginationContainer_query_1AHL8M\n}\n\nfragment DiscoverPaginationContainer_query_1AHL8M on Query {\n  photos: photoDiscoverSearch(first: 50, after: $cursor, filters: $filters, sort: $sort) {\n    edges {\n      node {\n        id\n        legacyId\n        canonicalPath\n        name\n        description\n        category\n        uploadedAt\n        location\n        width\n        height\n        isLikedByMe\n        notSafeForWork\n        tags\n        photographer: uploader {\n          id\n          legacyId\n          username\n          displayName\n          canonicalPath\n          avatar {\n            images {\n              url\n              id\n            }\n            id\n          }\n          followedBy {\n            totalCount\n            isFollowedByMe\n          }\n        }\n        images(sizes: [33, 35]) {\n          size\n          url\n          jpegUrl\n          webpUrl\n          id\n        }\n        pulse {\n          highest\n          id\n        }\n        __typename\n      }\n      cursor\n    }\n    totalCount\n    pageInfo {\n      endCursor\n      hasNextPage\n    }\n  }\n}\n',
    }
    # sending a request to 500px api for receiving some data
    response = requests.post('https://api.500px.com/graphql', cookies=cookies, headers=headers, json=json_data)
    res_json = response.json()


    # extracting url from res_json and appending it to a list
    for i in range(0,25):
        val = res_json['data']['photos']['edges'][i]["node"]['canonicalPath']
        url = 'https://500px.com' + val
        urls.append(url)


    # downloading pictures from urls in the list    
    for i in range(len(urls)):
        cont = download(url=urls[i], length=len(urls))
        open(f'{i}.jpg', 'wb').write(cont)
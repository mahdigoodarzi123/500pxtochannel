import requests

i=0
def download(urls):
        for i in range(len(urls)):
            result = requests.get(urls[i][0])
            # print(linke+'\n')
            

            #extracting the picture content and writing it to a jpg file for dowmloading it
            link_content = result.content
            open(f'{i}.jpg', 'wb').write(link_content)
            print("==================================================")
            print('[+] downloading from drscdn link: ' + urls[i][0])
            print("==================================================")
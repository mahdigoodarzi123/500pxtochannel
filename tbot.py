from time import sleep
from pyrogram import Client, filters
import os
from fiveoopx import fivehundreddl

# your api id and api hash
bot = Client(
    'ponsadpx',
    api_id=,
    api_hash=''
)


async def main():
    async with bot:
        datas = fivehundreddl()
        for i in range(0,23):

            #checking if the picture has nude content
            isnude = str(datas[i][1])
            # checking for being vertival or not
            vert = str(datas[i][2])


            if isnude == 'True' and vert == 'Vertical':
                #sending the picture with a caption
                await bot.send_photo(chat_id="@ponsadpx", photo=f'{i}.jpg', caption='#nude #mobile')
                print(f'[+] sent {i}.jpg (nude)(vertical)')
                # removing the picture after sending the photo
                os.remove(f'{i}.jpg')

            elif isnude == 'True':
                #sending the picture with a caption
                await bot.send_photo(chat_id="@ponsadpx", photo=f'{i}.jpg', caption='#nude')
                print(f'[+] sent {i}.jpg (nude)')
                # removing the picture after sending the photo
                os.remove(f'{i}.jpg')

            elif vert == 'Vertical':
                await bot.send_photo(chat_id="@ponsadpx", photo=f'{i}.jpg', caption='#mobile')
                print(f'[+] sent {i}.jpg (vertical)')
                os.remove(f'{i}.jpg')


            else:
                await bot.send_photo(chat_id="@ponsadpx", photo=f'{i}.jpg', caption='#desktop')
                print(f'[+] sent {i}.jpg')
                # removing the picture after sending the photo
                os.remove(f'{i}.jpg')



bot.run(main())
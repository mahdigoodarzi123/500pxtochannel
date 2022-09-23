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
        isnude = fivehundreddl()
        for i in range(0,23):

            #checking if the picture has nude content
            nude = str(isnude[i][1])


            if nude == 'True':
                #sending the picture with a caption
                await bot.send_photo(chat_id="@ponsadpx", photo=f'{i}.jpg', caption='#nude')
                print(f'[+] sent {i}.jpg (nude)')
                # removing the picture after sending the photo
                os.remove(f'{i}.jpg')


            else:
                await bot.send_photo(chat_id="@ponsadpx", photo=f'{i}.jpg')
                print(f'[+] sent {i}.jpg')
                # removing the picture after sending the photo
                os.remove(f'{i}.jpg')



bot.run(main())
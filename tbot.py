from time import sleep
from pyrogram import Client, filters
import os
from fiveoopx import fivehundreddl

# your api id and api hash
bot = Client(
    'ponsadpx',
    #your api hash and your api id
    api_id=,
    api_hash=''
)


async def main():
    async with bot:
        for i in range(0,25):
            try:
                # sending the picture to the channel
                await bot.send_photo(chat_id="@ponsadpx", photo=f'{i}.jpg')
                print(f'[+] sent {i}.jpg')
                # removing the picture after sending the photo
                os.remove(f'{i}.jpg')
            except:
                continue

try:
    fivehundreddl()
    sleep(5)
    bot.run(main())

except:
    sleep(5)
    bot.run(main())
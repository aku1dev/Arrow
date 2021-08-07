import os
import discord
from functions import *


TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
bot = discord.Client()


@bot.event
async def on_ready():
    print(
        f'{bot.user} is connected'
    )


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "873485624034877481" in message.content:  
        print("Mention detected".center(100, '-'))
        if 'ar' in message.content
            lang = 'ara'
        else:
            lang = 'eng'
        
        async for mes in message.channel.history(limit=200):
            if mes.attachments:
                url = str(mes.attachments[-1])
                if is_image(url):
                    print("Last image in channel detected".center(100, '-'))
                    try:
                        print("Getting OCR response".center(100, '-'))
                        response = process_image(url, lang).replace("|", "I").replace("\n", " ")
                        print("Text was successfully processed".center(100, '-'))
                        await message.channel.send(response, tts=True)
                    except:
                        await message.channel.send("Sorry, no text found.")
                    return
        await message.channel.send("No image found in the last 200 messages.")
                    

bot.run(TOKEN)

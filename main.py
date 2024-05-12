import os
import asyncio
import requests
import re
from pyrogram import Client, filters

#Use true boolean if you want to allow a rarity, and false if you want to disable it

session_string = os.getenv('SESSION_STRING')
api_hash = os.getenv('API_HASH')
api_id = os.getenv('API_ID')

app = Client("loli", api_id=api_id, api_hash=api_hash, session_string=session_string)
                    
hunt_bot = 6816539294
loot_bot = 6730565890
grab_bot = 5934263177
catch_bot = 6883098627
catcher_bot = 6195436879

@app.on_message(filters.photo & filters.group & filters.user(hunt_bot))
async def huntbot(bot, message):
    # Reply to the bot with the desired response
    await message.reply("/waifu@collect_waifu_cheats_bot")


@app.on_message(filters.photo & filters.group & filters.user(loot_bot))
async def lootbot(bot, message):
    # Reply to the bot with the desired response
    await message.reply("/waifu@collect_waifu_cheats_bot")



@app.on_message(filters.photo & filters.private & filters.user(grab_bot))
async def grabbot(bot, message):
    # Reply to the bot with the desired response
    await message.reply("/waifu@collect_waifu_cheats_bot")



@app.on_message(filters.photo & filters.private & filters.user(catch_bot))
async def catchbot(bot, message):
    # Reply to the bot with the desired response
    await message.reply("/waifu@collect_waifu_cheats_bot")



@app.on_message(filters.photo & filters.private & filters.user(catcher_bot))
async def catcherbot(bot, message):
    # Reply to the bot with the desired response
    await message.reply("/waifu@collect_waifu_cheats_bot")

app.run()

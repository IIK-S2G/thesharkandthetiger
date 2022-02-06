#!/usr/bin/env python3
import os
from dotenv import load_dotenv
#this is my first python script :D

import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = commands.Bot(command_prefix="!s2g")

@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_message(message):
    print("New message has come")
    ctx = client.get_context(message)
    if message.content == 'Hello':
        await ctx.send("Hello to you too!")

client.run(TOKEN)
import asyncio
import random
import re
import webbrowser

import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext import tasks
import requests

from g_image_puller import *
from commands import *

client = commands.Bot(command_prefix = 'm.', case_insensitive=True)

#a few sample commands and events

@client.event
async def on_ready():
    print('I AM READY!')
    
    
@client.command()
async def clear(ctx, user: discord.User, count: int):
   tmp = []
   if count > 50:
      maxDel = "The clear limit is 50 messages."
      e = discord.Embed()
      e.add_field(name="Clear limit.", value=maxDel, inline=False)
      await ctx.send(embed=e)
      return
   async for message in ctx.channel.history(limit=500):
      _user = message.author
      if _user == user:
         tmp.append(message)
   for delete in range(count+1):
      await tmp.pop(0).delete()
        

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server!')
    

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server...')
    

@client.command()
async def ping(ctx):
    await ctx.send(f'My ping is {client.latency}!')
    
    
@client.command()
async def hiya(ctx):
    await ctx.send('hey')
    
    
@client.command()
async def count(ctx):
    for i in range(1, 6):
        await ctx.send(f'{i} potato')
        

@client.command()
async def countdown(ctx):
    await ctx.send('3')
    await asyncio.sleep(1)
    await ctx.send('2')
    await asyncio.sleep(1)
    await ctx.send('1')
    await asyncio.sleep(1)
    holidays = ['Happy Thanksgiving!', 'Happy Hanukkah!', 'Merry Christmas!', 'Happy New Year!']
    for holiday in holidays:
        await ctx.send(random.choice(holidays))

    
client.run('t')

import asyncio 

import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext import tasks




client = commands.Bot(command_prefix = 'm.', case_insensitive=True)

#a few simple commands and events - note that the token is fake

@client.event
async def on_ready():
    print('I AM READY!')

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server!')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server...')

@client.command(alias=['yeet'])
async def ping(ctx):
    await ctx.send(f'My ping is {client.latency}!')
    
@client.command()
async def hiya(ctx):
    await ctx.send('hey')

client.run('Nzg5MTUxOTc5MjgwMTM4MjYw.X9t5DQ.L7c3iLvDNdIfp-T35G6kF8nNtVE')

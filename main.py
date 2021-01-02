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
    
@client.command()
async def count(ctx):
    for i in range(1, 6):
        await ctx.send(i, ' potato')

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
        
@client.command()
async def fact(ctx):
    #the following facts were taken from https://data-flair.training/blogs/facts-about-python-programming/ - Check it out!!
    pyfacts = ['''PYTHON WAS A HOBBY PROJECT - In December 1989, Python’s creator Guido Van Rossum was looking for a hobby project to keep him occupied in the week around Christmas.
               He had been thinking of writing a new scripting language that’d be a descendant of ABC and also appeal to Unix/C hackers. He chose to call it Python.''', '''WHY IT WAS CALLED PYTHON - The language’s name isn’t about snakes, but about the popular
British comedy troupe
Monty Python (from the 1970s).
Guido himself is a big fan of Monty Python’s Flying Circus. Being in a rather irreverent mood, he named the project ‘Python’. Isn’t it an interesting Python fact?''', '''NO BRACES AT ALL - Unlike Java and C++, Python does not use braces to delimit code.
Indentation is mandatory with Python. If you choose to import it from the __future__ package, it gives you a witty error (Not a chance).''', 'MULTIPLE RETURN VALUES - In Python, a function can return more than one value as a tuple.', '''MULTIPLE ASSIGNMENTS IN ONE STATEMENT - Python will let you assign
the same value to multiple variables in one statement.
It will also let you assign values to multiple variables at once.''', '''YAY, ANTIGRAVITY THAT\'S SO COOL! - If you get to the IDLE and type in import antigravity, it opens up a webpage with a comic about the antigravity module.''',
               '''PYTHON IS MORE POPULAR THAN FRENCH - According to a recent survey, in the UK in 2015, Python overtook French to be the most popular language taught in primary schools.
Out of 10, 6 parents preferred their children to learn Python over French. One of my favorite facts about Python programming.''',
               '''IDLE AS A CALCULATOR - Many people use the IDLE as a calculator. To get the value/result of the last expression, use an underscore.''']
    await ctx.send(random.choice(pyfacts))

client.run('Nzg5MTUxOTc5MjgwMTM4MjYw.X9t5DQ.L7c3iLvDNdIfp-T35G6kF8nNtVE')

import asyncio
import random
import re
import webbrowser

import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext import tasks
import requests

import g_image_puller

client = commands.Bot(command_prefix = 'm.', case_insensitive=True)

#a few simple commands and events

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
        
        
@client.command()
async def pfact(ctx):
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
    

@client.command()
async def fact(ctx):
    await ctx.send(re.search('<div id=\'z\'>(.*?).<br/><br/>',
           requests.get('http://randomfactgenerator.net/').text).group(1))
    

#The 'wrapper', I guess for g_image_puller.py - See the module in my WebFuncs repo 
@client.command()    
async def image(ctx, image):
    result = google_image(image)
    await ctx.send(webbrowser.open(result))
    
    
@client.command()
async def meme(ctx):
    meme = google_image('meme')
    await ctx.send('A meme from the internet (probably rly bad, sry): ' + meme)
    

@client.command()
async def get_meme(ctx, amount=1):
    viewed = []
    count = 0
    with requests.session() as s:
        headers = {
                   "user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36"}
        for x in range(amount):
            url =  "https://www.memecenter.com"
            data = s.get(url, headers=headers).text
            count +=1
            find_meme_url = re.search("<a href=\"(.*?)\" class=\"hvm-d-item random\">Surprise Me!</a>", data).group(1)
            find_meme_image = s.get(find_meme_url, headers=headers).text
            try:
                img = re.search("<a href=\"(.*?)\" rel=\"nofollow\"", find_meme_image).group(1)
                if img not in viewed:
                   viewed.append(img)
            except: pass
            
        await ctx.send(viewed[0])
    

    
client.run('t')

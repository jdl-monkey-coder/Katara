import asyncio
import random
import re
import webbrowser
import os
import html

import discord
from discord import Color
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext import tasks
import requests

#all modules unrecognized are solely from my own device
from g_image_puller import *
from GitHubModule import github
from YouTubeModule import Youtube


client = commands.Bot(command_prefix = ['@'], case_insensitive=True)

@client.command()
async def pfact(ctx):
    #the following facts were taken from https://data-flair.training/blogs/facts-about-python-programming/ - Check it out!!
    pyfacts = ['''PYTHON WAS A HOBBY PROJECT - In December 1989, Python’s creator Guido Van Rossum was looking for a hobby project to keep him occupied in the week around Christmas.
               He had been thinking of writing a new scripting language that’d be a descendant of ABC and also appeal to Unix/C hackers. He chose to call it Python.''', '''WHY IT WAS CALLED PYTHON - The language’s name isn’t about snakes, but about the popular
British comedy troupe
Monty Python (from the 1970s).
Guido himself is a big fan of Monty Python’s Flying Circus. Being in a rather irreverent mood, he named the project ‘Python’. Isn’t it an interesting Python fact?''', '''NO BRACES AT ALL - Unlike Java and C++, Python does not use braces to delimit code.
Indentation is mandatory with Python. If you choose to import it from the `__future__` package, it gives you a witty error (Not a chance).''', 'MULTIPLE RETURN VALUES - In Python, a function can return more than one value as a tuple.', '''MULTIPLE ASSIGNMENTS IN ONE STATEMENT - Python will let you assign
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


@client.command()    
async def image(ctx, image):
    img = google_image(image)
    await ctx.send(os.system(f'start {img}'))
    await ctx.send('Check your web browser!')

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


@client.command()
async def _8ball(ctx, *, question):
    responses = ['It is certain',
                 'It is decidedly so',
                 'Without a doubt',
                 'Yes - definitely',
                 'You may rely on it',
                 'As I see it, yes',
                 'Most likely',
                 'Outlook good',
                 'Yes',
                 'Signs point to yes',
                 'Ask again later',
                 'Cannot predict now',
                 'Concentrate and ask again',
                 'Don’t count on it',
                 'Outlook not so good',
                 'Reply hazy, try again',
                 'Very doubtful',
                 'My sources say no',
                 'My reply is no',
                 'Better not tell you now'
                 ]

    await ctx.send(random.choice(responses))


@client.command()
async def joke(ctx):
    pass


#TODO: UPDATE EVERY DAY
@client.command()
async def getRandomThing(ctx, lines: int):
    randomThing = requests.get('https://goalkicker.com/JavaBook/')
    await ctx.send(randomThing.text[:lines])


@client.command()
async def hi(ctx, name):
    await ctx.send(f"hi, {name}!")


yt = Youtube()

#YouTube commands, wraps methods from the Youtube class

@client.command()
async def getRandom(ctx, search):
    await ctx.send(yt.getRandom(search))


@client.command()
async def getFirst(ctx, search):
    await ctx.send(yt.getFirst(search))


query = github()

#GitHub commands

#avatar
#followers
#repo_count
#organization
#username
#following
#stars
#website
#name
#description
#location
#joined:
#url


@client.command()
async def github(ctx, user, key):
   data = query.getUser(user)
   if key in data:
     await ctx.send(data[key])
   else: await ctx.send("Invalid key")


@client.command()
async def githubUser(ctx, user):
    await ctx.send("\n".join([f"{k} : {v}" for k, v in query.getUser(user).items()]))
    
 
client.run('Nzg5MTUxOTc5MjgwMTM4MjYw.X9t5DQ.Tdc2aDWxwYLZZZPh28ZVLflJwWA')

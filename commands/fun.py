import re
import os
import webbrowser
import random
import html

from discord.ext import commands
import requests

from g_image_puller import *


client = commands.Bot(command_prefix = ['m.', '@', ''], case_insensitive=True)

#These commands are only here, on the GitHub in the commands folder for the sake of organization. In my actual code editor, the commands are all in bot.py...lol
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


@client.command()    
async def image(ctx, image):
    result = google_image(image)
    await ctx.send(webbrowser.open(result))
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
            
            
@client.command()
async def eightball(ctx, question):
    eightball_rsp = ['no, just no',
                 'yes, absoLUTEly',
                 'eh... I don\'t think so!',
                 'Go for it!', 'yesss',
                 'nonono DO NOT DO THAT',
                 'think again!',
                 'yes, do it!!']
    await ctx.send(random.choice(eightball_rsp))
            
        await ctx.send(viewed[0])
       
    
#TODO: UPDATE EVERY DAY
@client.command()
async def getRandomThing(ctx, lines: int):
    randomThing = requests.get('https://automatetheboringstuff.com/files/rj.text')
    await ctx.send(randomThing.text[:lines])


@client.command()
async def hi(ctx, name):
    await ctx.send(f"hi, {name}!")
    

'''
Youtube module that doesn't require an API Key.
By: ᴶᵉˢˢ#8302

NOTE: 
There may be some bugs with Like/Dislike
i'll fix it at some point.
'''
class Youtube:

    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
        self.video_ids = []
    
    def _search(self, query):
        ''' Helper function for search requests '''
        self.video_ids.clear()
        with requests.session() as s:
            try:
              req = s.get(f'https://www.youtube.com/results?search_query={query}', headers = self.headers).text
              for yid in [_id for _id in re.findall('i.ytimg.com/vi/(.*?)/', req) if len(_id) ==  11]:
                  if yid not in self.video_ids:
                      self.video_ids.append(yid)
              return self.video_ids
            except Exception as e:
                print(f'Error: {e}')

    def _numeric(self, data):
        ''' Helper function that removes non numeric data from string '''
        return "".join([x for x in data if x.isnumeric()])
                
        
    def getRandom(self, search=None):
         ''' Returns a random video from self.videos '''
         if search:
            self._search(search)
         else: pass
         if len(self.video_ids) > 0:
             return f'https://www.youtube.com/watch?v={random.choice(self.video_ids)}'
         else: return None
            

    def getFirst(self, search=None):
         ''' Returns the first video from self.videos '''
         if search:
            self._search(search)
         else: pass
         if len(self.video_ids) > 0:
             return f'https://www.youtube.com/watch?v={self.video_ids[0]}'
         else: return None


yt = Youtube()

#YouTube commands, wraps methods from the Youtube class

@client.command()
async def getRandom(ctx, search):
    await ctx.send(yt.getRandom(search))


@client.command()
async def getFirst(ctx, search):
    await ctx.send(yt.getFirst(search))

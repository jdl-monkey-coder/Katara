import requests
import random
import re
import html

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
                
    def getInfo(self, _id):
        ''' Returns info about a video {} '''
        if len(_id) == 11:
            _id = 'https://www.youtube.com/watch?v={_id}'
        else: pass
        with requests.session() as s:
            try:
              data = s.get(_id, headers = self.headers).text
              like_dislike_data = re.findall('{"accessibilityData":{"label":"(.*?)"}', data)
              info = {"title":  re.search("<title>(.*?)</title>", data).group(1)[:-10],
                      "url": _id,
                      "uploader": re.search('"name": "(.*?)"', data).group(1),
                      "views": re.search('<meta itemprop="interactionCount" content="(.*?)">', data).group(1),
                      "likes": self._numeric(like_dislike_data[0]),
                      "dislikes": self._numeric(like_dislike_data[3]),
                      "description": re.search('<meta property="og:description" content="(.*?)">', data).group(1),
                      "thumbnail": f"https://i.ytimg.com/vi/{_id.split('watch?v=',1)[1]}/hq720.jpg"
                      }
              return {k: html.unescape(v) for k, v in info.items()}              
            except: return None
            
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

    def getVideos(self, search=None):
         ''' Returns all video urls [] '''
         if search:
            self._search(search)
         else: pass
         if len(self.video_ids) > 0:
            return [f'https://www.youtube.com/watch?v={x}' for x in self.video_ids]
         else:
            return None

    def getIds(self, search=None):
        ''' Returns all video IDS [] '''
        if search:
           self._search(search)
        else: pass
        if len(self.video_ids) > 0:
           return self.video_ids
        else: return None


if __name__ == '__main__':
    yt = Youtube()
    tests = [
      "Testing: getting info from video",
      yt.getInfo('https://www.youtube.com/watch?v=sT6Di6UERxw'),
      "Testing: getting the first video from query 'Cats'",
      yt.getFirst("Cats"),
      "Testing: getting a random video from query 'Dogs'",
      yt.getRandom("Dogs")
    ]
    for test in tests: print(test, "\n")

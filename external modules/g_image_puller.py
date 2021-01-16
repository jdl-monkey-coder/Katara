#pulls images from the web

import re
import requests
import random

def google_image(*args):
    args = " ".join(args)
    with requests.session() as s:
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
        d = s.get("https://www.google.com/search?q=%s&tbm=isch" % args, headers = headers).content
        container = [x.split('["')[-1].split('",')[0] for x in re.findall('\[(.*?)rgb', str(d)) if ((".jpg" in x) or (".gif" in x) or (".png" in x)) and (("https:" in x) or ("http:" in x)) and "google" not in x]
        return random.choice(container)

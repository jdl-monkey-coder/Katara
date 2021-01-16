import re
import requests

'''
- Title
A Github user info wrapper that requires no API key.
>> Pulls information with a username query.

- Author
ᴶᵉˢˢ#8302

- How to use.
github.getUser(username)
>> returns a dict with all the available data.

- Getters
Takes an optional username parameter.
>> getters -> getAvatar, getUsername, getName
>> getters -> getFollowers, GetFollowing, getDescription
>> getters -> get_repo_count, getStars, getLocation,
>> getters -> getOrganization, getWebsite, getJoined, getUrl
'''

class github:

    def __init__(self):
        self.__avatar = None
        self.__username = None
        self.__name = None
        self.__followers = None
        self.__following = None
        self.__description  = None
        self.__repo_count = None
        self.__stars = None
        self.__location = None
        self.__organization = None
        self.__website = None
        self.__joined = None
        self.__url = None
        self.request_url = 'https://github.com/'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36'}
        
    def getUser(self, user):
        with requests.session() as s:
            try:
                data = s.get(f'{self.request_url}{user}', headers = self.headers).text
                try:
                  self.__url = f'{self.request_url}{user}'
                except: self.__url = None
                try:
                  self.__username = user
                except: self.__username = None
                try:
                  self.__name = re.search('<title>(.*?)</title>', data).group(1).split('(', 1)[1].split(')', 1)[0].strip()
                except: self.__name = None
                try:
                  self.__repo_count = re.search('class="Counter ">(.*?)</span>', data).group(1)
                except: self.__repo_count = None
                try:
                  self.__stars = re.search('<span class="text-bold text-gray-dark">(.*?)</span>', data).group(1)
                except: self.__stars = None
                try:
                  self.__followers, self.__following = re.findall('<span class="text-bold text-gray-dark" >(.*?)</span>', data)
                except: self.__followers, self.__following = (None, None)
                try:
                  self.__description = data.split('<meta name="twitter:description" content="', 1)[1].split('" />', 1)[0].split(f'{user} has', 1)[0]
                except: self.__description = None
                try:
                  self.__location = re.search('aria-label="Home location:(.*?)">', data).group(1).strip()
                except: self.__location = None
                try:
                  self.__organization = re.search('aria-label="Organization: (.*?)">', data).group(1).strip()
                except: self.__organization = None
                try:
                  self.__website = re.search('<a rel="nofollow me" class="link-gray-dark " href="(.*?)">', data).group(1).strip()
                except: self.__website = None
                try:
                  self.__joined = re.search('class="no-wrap">(.*?)</relative-time>', data).group(1)
                except: self.__joined = None
                try:
                  self.__avatar = re.search('<meta property="og:image" content="(.*?)"', data).group(1)
                except: self.__avatar = None
                return {"avatar": self.__avatar, "username": self.__username, "name": self.__name,
                        "followers": self.__followers,"following": self.__following, "description": self.__description,
                        "repo_count": self.__repo_count, "stars": self.__stars, "location": self.__location,
                        "organization": self.__organization, "website": self.__website, "joined:": self.__joined, "url": self.__url}
            except:
                 return False

    def getAvatar(self, user=None):
        if not user:
            return self.__avatar
        else:
            self.getUser(user)
            return self.__avatar
        
    def getUsername(self, user=None):
        if not user:
            return self.__username
        else:
            self.getUser(user)
            return self.__username

    def getName(self, user=None):
        if not user:
            return self.__name
        else:
            self.getUser(user)
            return self.__name    
        
    def getFollowers(self, user=None):
        if not user:
            return self.__followers
        else:
            self.getUser(user)
            return self.__followers
        
    def getFollowing(self, user=None):
        if not user:
            return self.__following
        else:
            self.getUser(user)
            return self.__following
        
    def getDescription(self, user=None):
        if not user:
            return self.__description
        else:
            self.getUser(user)
            return self.__description
        
    def get_repo_count(self, user=None):
        if not user:
            return self.__avatar
        else:
            self.getUser(user)
            return self.__avatar

    def getStars(self, user=None):
        if not user:
            return self.__stars
        else:
            self.getUser(user)
            return self.__stars

    def getLocation(self, user=None):
        if not user:
            return self.__location
        else:
            self.getUser(user)
            return self.__location

    def getOrganization(self, user=None):
        if not user:
            return self.__organization
        else:
            self.getUser(user)
            return self.__organization

    def getWebsite(self, user=None):
        if not user:
            return self.__website
        else:
            self.getUser(user)
            return self.__website

    def getJoined(self, user=None):
        if not user:
            return self.__joined
        else:
            self.getUser(user)
            return self.__joined
        
    def getUrl(self, user=None):
        if not user:
            return self.__url
        else:
            self.getUser(user)
            return self.__url

if __name__ == '__main__':
    git = github()
    print(git.getUser('jdl-monkey-coder'))

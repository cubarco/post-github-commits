import oauth2
import urllib

class SocialPlt:
    def __init__(self, ckey, cscr, akey, ascr, url):
        self.url = url
        self.consumer = oauth2.Consumer(key=ckey, secret=cscr)
        self.token = oauth2.Token(key=akey, secret=ascr)
        self.client = oauth2.Client(self.consumer, self.token)

    def req(self, http_method="POST", post_body=None):
        resp, content = self.client.request(self.url, method=http_method, body=post_body)
        return content


class Twitter(SocialPlt):
    def __init__(self, ckey, cscr, akey, ascr, url):
        SocialPlt.__init__(self, ckey, cscr, akey, ascr, url)
        self.post_body_tem = {"status": None} 
    
    def req(self, http_method="POST", text=None):
        self.post_body_tem["status"] = text
        SocialPlt.req(self, http_method, post_body=urllib.urlencode(self.post_body_tem))

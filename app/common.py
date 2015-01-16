import oauth2
import urllib
import urllib2

class Twitter:
    def __init__(self, ckey, cscr, akey, ascr, url):
        self.url = url
        self.consumer = oauth2.Consumer(key=ckey, secret=cscr)
        self.token = oauth2.Token(key=akey, secret=ascr)
        self.client = oauth2.Client(self.consumer, self.token)

    def req(self, text=None):
        post_body = urllib.urlencode({"status": text})
        resp, content = self.client.request(self.url, method="POST", body=post_body)
        return content

class Facebook:
    def __init__(self, access_token, url):
        self.url = url
        self.post_body_dic = {"access_token": access_token}

    def req(self, text=None):
        self.post_body_dic["message"] = text
        post_body = urllib.urlencode(self.post_body_dic)
        req = urllib2.Request(self.url, post_body)
        resp = urllib2.urlopen(req)
        return resp.read()

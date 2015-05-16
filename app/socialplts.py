import oauth2
import urllib
import urllib2
import json


class Twitter:
    def __init__(self, ckey, cscr, akey, ascr, url):
        self.url = url
        self.consumer = oauth2.Consumer(key=ckey, secret=cscr)
        self.token = oauth2.Token(key=akey, secret=ascr)
        self.client = oauth2.Client(self.consumer, self.token)

    def req(self, text=None):
        post_body = urllib.urlencode({"status": text})
        try:
            resp, content = self.client.request(self.url, method="POST",
                                                body=post_body)
        except:
            pass
        else:
            error_json = json.loads(content).get("errors")
            if not error_json:
                return {'status': 'succeed', 'name': 'Twitter'}

        return {
                'status': 'failed',
                'name': "Twitter",
        }


class Facebook:
    def __init__(self, access_token, url):
        self.url = url
        self.post_body_dic = {"access_token": access_token}

    def req(self, text=None):
        self.post_body_dic["message"] = text
        post_body = urllib.urlencode(self.post_body_dic)
        req = urllib2.Request(self.url, post_body)
        try:
            resp = urllib2.urlopen(req)
        except:
            pass
        else:
            error_json = json.loads(resp.read()).get("error")
            if not error_json:
                return {'status': 'succeed', 'name': 'Facebook'}

        return {
                'status': 'failed',
                'name': 'Facebook',
        }

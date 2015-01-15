#!/usr/bin/python
# coding=utf8

from config import *
import json
import re
import hmac
import hashlib
import bottle
from bottle import HTTPResponse

app = application = bottle.Bottle()

@app.post('/')
def default():
    sig_header = bottle.request.get_header("X-Hub-Signature")
    req_body = bottle.request.body.read()
    sig = hmac.new(WEBHOOK_KEY, msg=req_body, 
            digestmod=hashlib.sha1).hexdigest()
    if "sha1=" + sig != sig_header:
        return HTTPResponse(status=403, body="bad signature\n")

    event = bottle.request.get_header("X-GitHub-Event")
    if event != "push":
        return HTTPResponse(status=501, body="not implemented\n")

    messages = [i.get("message") for i in json.loads(req_body).get("commits")]
    titles = []
    for message in messages:
        title = re.findall(COMMIT_REGX, message)
        if len(title) > 0:
            titles.append(title[0])

    for title in titles:
        for social_plt in SOCIAL_PLTS:
            post_text = POST_TEXT % title
            social_plt.req(text=post_text)

    return "ok\n"

if __name__ == "__main__":
    bottle.run(app=app, host='0.0.0.0', port=8080)

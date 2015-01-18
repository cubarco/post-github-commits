from socialplts import * 

# Required
SOCIAL_PLTS = [
            Twitter(
                    ckey="CONSUMER_KEY",
                    cscr="CONSUMER_SECRET",
                    akey="ACCESS_KEY",
                    ascr="ACCESS_SECRET",
                    url="https://api.twitter.com/1.1/statuses/update.json",
            ),
            Facebook(
                     access_token="ACCESS_TOKEN",
                     url="https://graph.facebook.com/me/feed",
            ),
]

# Required
WEBHOOK_KEY = "Github webhook key"

POST_TEXT = u"[TEST] I posted a new blog: \"%s\". (Site: https://url.to-your.site)"

# Commit message example: "post Hello, world"
COMMIT_REGX = r'^(?i)post (.*)'

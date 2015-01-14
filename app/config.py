from common import * 

social_plts = [
            Twitter(
                ckey="CONSUMER_KEY",
                cscr="CONSUMER_SECRET",
                akey="ACCESS_KEY",
                ascr="ACCESS_SECRET",
                url="https://api.twitter.com/1.1/statuses/update.json",
                ),
        ]

POST_TEXT = "[TEST] I have a new post on my blog: \"%s\". (Site: https://url.to-your.site)"

WEBHOOK_KEY = "Github webhook key"

COMMIT_REGX = r'^(?i)post (.*)'

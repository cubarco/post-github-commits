post-github-commits
===
This is a web backend that handles events triggered by Github Webhooks. This
program plays the role that parse the commit message sent from Github Webhook 
according to a given regex pattern and then post to social platforms. At present,
this only supports Twitter.

Configuration
---
You can use `uwsgi` to route requests.

For more information, see config.py.

Requirements
---
see requirements.txt

License
---
[GPLv2](http://www.gnu.org/licenses/gpl-2.0.html)

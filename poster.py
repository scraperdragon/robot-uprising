#!/usr/bin/env python
import requests
import json
import datetime
import pytz

bst = pytz.timezone('Europe/London')
utc_time = datetime.datetime.now()
uk_datetime = pytz.utc.localize(utc_time).astimezone(bst)
uk_strtime = uk_datetime.strftime("%H:%M")

really_standup = uk_datetime.hour == 9 and uk_datetime.minute > 45
if not really_standup:
    print "Not standup yet..."
    #exit()


url = open("/home/tool/secret_webhook.url", "r").read().strip()
msg = "It's {} and time for <https://tinyurl.com/pearbot|standup!>".format(uk_strtime)

payload = json.dumps({"text": msg,
                      "username": "robot-uprising",
                      "icon_emoji": ":alarm_clock:",
                      "channel": "@dragon"
                    })

requests.post(url, data = payload)

import requests
import json


def send_sms(number,message):
    url = 'https://www.fast2sms.com/dev/bulkV2'
    params={
        'authorization':'gKLR3Dn0JGko5Bq1O4hfewENVSXsFPM9TbAZdzCvm7lIiHQ2xcpDkS4Njus0ZVO6xmh2tb3yQFGRA9JY',
        'sender_id':'sender_id',
        'message':message,
        'language':'english',
        'route': 'p',
        'numbers': number,
    }
    response = requests.get(url, params=params)
    dic = response.json()
    print(dic)


send_sms("9877685627","This is message")
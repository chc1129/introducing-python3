menu = \
{
"breakfast": {
        "hours": "7-11",
        "items": {
                "breakfast burritos": "$6.00",
                "pancakes": "$4.00"
                }
        },
"lunch" : {
        "hours": "11-3",
        "items": {
                "hamburger": "$5.00"
                }
        },
"dinner": {
        "hours": "3-10",
        "items": {
            "spagehtti": "$8.00"
            }
        }
}

import json
menu_json = json.dumps(menu)
print(menu_json)

menu2 = json.loads(menu_json)
print(menu2)

import datetime
now = datetime.datetime.utcnow()
print(now)
#print(json.dumps(now))

now_str = str(now)
print(json.dumps(now_str))
from time import mktime
now_epoch = int(mktime(now.timetuple()))
print(json.dumps(now_epoch))

class DTEncoder(json.JSONEncoder):
    def default(self, obj):
        # isinstance()はobjの型をチェックする
        if isinstance(obj, datetime.datetime):
            return int(mktime(obj.timetuple()))
        # でなければ,通常のデコーダの処理を行う
        return json.JSONEncoder.default(self, obj)

print(json.dumps(now, cls=DTEncoder))

print(type(now))
print(isinstance(now, datetime.datetime))
print(type(234))
print(isinstance(234, int))
print(type('hey'))
print(isinstance('hey', str))

import simplejson as json

data = '''{
"code": 2,
"data":
{
"tags_str": "",
"tags": "1231",
"job": 0,
"sex": 0,
"phone": "",
"birthday": "1985-01-01",
"location": "",
"company": "",
"slogan": "",
"introduction": "",
"avatar": "/static/fruit_avatar/Fruit-15.png",
"gravatar": "https://dn-coding-net-avatar.qbox.me/89628160-f594-4e52-8c77-fda089fcc7dd.jpg",
"lavatar": "/static/fruit_avatar/Fruit-15.png",
"created_at": 1426579942000,
"last_logined_at": 1426579942000,
"last_activity_at": 1426580037625,
"global_key": "baoti",
"name": "baoti",
"name_pinyin": "",
"updated_at": 1426579942000,
"path": "/u/baoti",
"status": 1,
"email": "niuniu@yahoo.com",
"is_member": 0,
"id": 85544,
"follows_count": 2,
"fans_count": 3,
"tweets_count": 6,
"followed": false,
"follow": false
}
}
'''
data = json.loads(data)
print(data.get('code') != 1)

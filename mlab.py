import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds233596.mlab.com:33596/saleweb
host = "ds233596.mlab.com"
port = 33596
db_name = "saleweb"
user_name = "admin"
password = "admin123"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password,retryWrites= False)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
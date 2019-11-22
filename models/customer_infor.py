from mongoengine import Document,StringField,IntField,EmailField,ListField
class Customerinfor(Document):
    name = StringField()
    numberphone = StringField()
    mail = EmailField()
    city = StringField()
    district = StringField()
    address = StringField()
    listordered = ListField()
    total = IntField()
    count = IntField()
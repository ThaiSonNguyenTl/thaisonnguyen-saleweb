from mongoengine import Document,StringField,IntField,EmailField
class Customerinfor(Document):
    name = StringField()
    numberphone = StringField()
    mail = EmailField()
    city = StringField()
    district = StringField()
    address = StringField()
    title = StringField()
    price = IntField()
    image = StringField()
    count = IntField()
    size = StringField()
    total = IntField()
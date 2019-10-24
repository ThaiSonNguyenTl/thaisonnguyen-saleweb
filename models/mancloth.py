from mongoengine import Document,StringField , IntField
class Mancloth(Document):
    title = StringField()
    image = StringField()
    price = IntField()
   
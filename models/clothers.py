from mongoengine import Document,StringField , IntField
class Clothers(Document):
    title = StringField()
    image = StringField()
    price = IntField()
   
from mongoengine import *

connect(host='mongodb+srv://kseniiavoitko:kJwOlfANt8JTrQ1S@kseniia.fbnhbdy.mongodb.net/learnMongoDB', ssl=True)

class Authors(Document):
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()

class Qoutes(Document):
    tags = ListField(StringField(max_length=30))
    author = ReferenceField(Authors, reverse_delete_rule=CASCADE)
    quote = StringField()
    
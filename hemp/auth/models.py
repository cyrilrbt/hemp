import mongoengine as db


class User(db.Document):
    name = db.StringField(max_length=100, required=True)
    email = db.EmailField(max_length=100, required=True)

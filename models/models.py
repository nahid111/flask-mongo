from datetime import datetime
from app_extensions import db


class User(db.Document):
    first_name = db.StringField(max_length=50, required=True, unique=True)
    last_name = db.StringField(max_length=50)
    created_at = db.DateTimeField(default=datetime.utcnow)

    meta = {
        'allow_inheritance': True,
        'indexes': [
            '-created_at'
        ]
    }

    def __repr__(self):
        return '<User %r>' % self.first_name


class Address(db.EmbeddedDocument):
    street = db.StringField()
    city = db.StringField(max_length=50)
    state = db.StringField(max_length=50)
    zip = db.IntField()


class Parent(User):
    address = db.EmbeddedDocumentField(Address)


class Child(User):
    parent = db.ReferenceField(Parent, reverse_delete_rule=db.CASCADE)

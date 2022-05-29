
import datetime
import uuid

from mongoengine import fields, document


class ProviderCollection(document.DynamicDocument):
    row_id = fields.UUIDField(primary_key=True, default=uuid.uuid4)
    name = fields.StringField(required=True)
    email = fields.StringField(required=True, unique=True)
    phone_number = fields.StringField()
    lang = fields.StringField(required=True)
    currency = fields.StringField(required=True)
    created_at = fields.DateField(default=datetime.datetime.now, required=True)
    meta = {
        'indexes': [
            'name', 'email'
        ],
        'collection': 'provider'
    }


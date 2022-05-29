
import datetime
import uuid

from mongoengine import fields, document


class ServiceAreaCollection(document.DynamicDocument):
    row_id = fields.UUIDField(primary_key=True, default=uuid.uuid4)
    name = fields.StringField(required=True)
    h_three_geo_hash = fields.StringField(required=True)
    price = fields.FloatField(required=True)
    polygon = fields.PolygonField(required=True)
    created_at = fields.DateField(default=datetime.datetime.now, required=True)
    meta = {
        'indexes': [
            'name', 'h_three_geo_hash'
        ],
        'collection': 'service_area'
    }


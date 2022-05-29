from mongoengine import connect

from jeo_services import config

connect(host=config.MONGO_URL)
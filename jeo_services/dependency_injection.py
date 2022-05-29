from injector import singleton, Injector

from jeo_services.core.adapters.mongo.provider import MongoProviderAdapter
from jeo_services.core.adapters.mongo.service_area import MongoServiceAreaAdapter
from jeo_services.core.biz.service_area import ServiceAreaService
from jeo_services.core.ports.provider import ProviderPort
from jeo_services.core.ports.service_area import ServiceAreaPort


def configure(binder):
    binder.bind(ProviderPort, to=MongoProviderAdapter, scope=singleton)
    binder.bind(ServiceAreaPort, to=MongoServiceAreaAdapter, scope=singleton)
    binder.bind(ServiceAreaService, to=ServiceAreaService, scope=singleton)


factory = Injector(configure)

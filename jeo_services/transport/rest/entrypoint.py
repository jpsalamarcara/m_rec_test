from fastapi import FastAPI

from jeo_services.transport.rest.routes import providers, service_areas

app = FastAPI(
    title='Jeo Services',
    docs_url='/docs',
    redoc_url='/redoc',
    root_path=''
)


app.include_router(providers.router, prefix='/v1/providers', tags=['provider'])
app.include_router(service_areas.router, prefix='/v1/service_areas', tags=['service_areas'])

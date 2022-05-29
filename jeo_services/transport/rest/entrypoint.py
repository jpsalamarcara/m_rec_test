from fastapi import FastAPI

from jeo_services.transport.rest.routes import providers

app = FastAPI(
    title='Jeo Services',
    docs_url='/docs',
    redoc_url='/redoc',
    root_path=''
)


app.include_router(providers.router, prefix='/v1/providers', tags=['provider'])

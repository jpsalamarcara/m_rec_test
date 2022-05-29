# Jeo Services by JuanP

This application follows a hexagonal architecture, so, in the `core` folder you will
find  `domain, ports, biz and adapters`.
In the `ports folder` are all the abstract definitions and in the `adapters folder` are the implementations of those
abstractions.
The dependency injection is responsible for choosing the right adapter at runtime.

In the `transport folder` you will find all the REST API details implemented using FastAPI

## For running tests

```shell
docker-compose -f docker/testing.yml up
pytest tests/
```

## For demo in local with docker

```shell
sh build.sh
docker-compose -f docker/production.yml up
# go to http://localhost/docs
```

## Example for service area

POST /v1/service_areas
```json
{
"name": "my_area",
"price": 3000,
"polygon": { "type": "Polygon",
    "coordinates": [[
    [17.60083012593064, 78.18557739257812],
    [17.16834652544664, 78.19381713867188],
    [17.17490690610013, 78.739013671875],
    [17.613919673106714, 78.73489379882812],
    [17.60083012593064, 78.18557739257812]]]
    },
"provider_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
}
```
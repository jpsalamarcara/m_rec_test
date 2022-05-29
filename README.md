# Jeo Services by JuanP

This application follows a hexagonal architecture, so, in the `core` folder you will find  `domain, ports, biz and adapters`.
In the `ports folder` are all the abstract definitions and in the `adapters folder` are the implementations of those abstractions.
The dependency injection is responsible for choosing the right adapter at runtime.

In the `transport folder` you will find all the REST API details implemented using FastAPI
FROM python:3.9
WORKDIR /jeo
COPY ./dist/jeo_services-0.1.0-py3-none-any.whl /jeo/
RUN python3 -m pip install /jeo/jeo_services-0.1.0-py3-none-any.whl
CMD ["uvicorn", "jeo_services.transport.rest.entrypoint:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]
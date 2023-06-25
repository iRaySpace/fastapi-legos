import os
import importlib
from fastapi.routing import APIRouter


def _create_endpoints(router: APIRouter, cls, prefix):
    default_endpoints = [
        ('get', prefix, 'get_all', 'Read all'),
        ('get', prefix + '/{id}', 'get', 'Read'),
        ('post', prefix, 'post', 'Create'),
        ('put', prefix + '/{id}', 'put', 'Update'),
        ('delete', prefix + '/{id}', 'delete', 'Delete'),
    ]
    for router_method, path, cls_method, summary in default_endpoints:
        endpoint = getattr(cls, cls_method, None)
        if endpoint:
            endpoint_generator = getattr(router, router_method)
            endpoint_generator(path)(endpoint)


def get_router():
    router = APIRouter()
    # Do not put anything under `template/doctype` except doctype functionalities, this will break!
    doctypes = [f.name for f in os.scandir('template/doctype') if f.is_dir() and f.name != '__pycache__']
    for doctype in doctypes:
        doctype_module = importlib.import_module(f'template.doctype.{doctype}.{doctype}')
        doctype_class = getattr(doctype_module, doctype.capitalize())
        _create_endpoints(router, doctype_class, f'/{doctype}')
    return router

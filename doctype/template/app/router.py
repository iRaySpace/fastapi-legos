import os
import importlib
from fastapi.routing import APIRouter


def _create_endpoints(router: APIRouter, cls, prefix):
    default_endpoints = [
        ('get', prefix, 'get_all', 'Read all'),
        ('get', prefix, 'get', 'Read'),
        ('post', prefix, 'post', 'Create'),
        ('post', prefix, 'put', 'Update'),
        ('delete', prefix, 'delete', 'Delete'),
    ]
    for router_method, path, cls_method, summary in default_endpoints:
        print(router_method, path, cls_method, summary) 


def get_router():
    router = APIRouter()
    # Do not put anything under `template/doctype` except doctype functionalities, this will break!
    doctypes = [f.name for f in os.scandir('template/doctype') if f.is_dir() and f.name != '__pycache__']
    for doctype in doctypes:
        doctype_module = importlib.import_module(f'template.doctype.{doctype}.{doctype}')
        doctype_class = getattr(doctype_module, doctype.capitalize())
        _create_endpoints(router, doctype_class, f'/{doctype}')
    return router

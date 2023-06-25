import os
import importlib
from fastapi.routing import APIRouter
from cookiecutter.main import cookiecutter


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


def _process_doctype_endpoint(name: str):
    module_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    root_dir = os.path.dirname(module_dir)
    context = {'name': name, 'name_capitalized': name.capitalize()} 
    cookiecutter(
        os.path.join(root_dir, 'boilerplate'),
        output_dir=os.path.join(module_dir, 'doctype'),
        extra_context=context,
        no_input=True,
    )
    return context


def get_router():
    router = APIRouter()
    router.post('/')(_process_doctype_endpoint)
    # Do not put anything under `template/doctype` except doctype functionalities, this will break!
    doctypes = [f.name for f in os.scandir('template/doctype') if f.is_dir() and f.name != '__pycache__']
    for doctype in doctypes:
        doctype_module = importlib.import_module(f'template.doctype.{doctype}.{doctype}')
        doctype_class = getattr(doctype_module, doctype.capitalize())
        _create_endpoints(router, doctype_class, f'/{doctype}')
    return router

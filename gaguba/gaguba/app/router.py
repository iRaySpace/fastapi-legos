from fastapi.routing import APIRouter
from gaguba.domain.dto import PaymentCreateDto
from gaguba.domain import usecase
from gaguba.data import payment_repository

api_router = APIRouter()


@api_router.get('/ping')
async def send_pong():
    return {'message': 'pong'}


@api_router.get('/payments')
async def send_payments():
    return []


@api_router.post('/payments')
async def process_payments(payment: PaymentCreateDto):
    return usecase.create_payment(payment_repository, payment)

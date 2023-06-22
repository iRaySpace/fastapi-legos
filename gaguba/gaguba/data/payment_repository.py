import uuid
from typing import List
from gaguba.domain.entity import Payment

data = []


def get_all() -> List[Payment]:
    return data


def create(payment: Payment):
    new_payment = Payment(**{
        **payment.dict(by_alias=True),
        'id': str(uuid.uuid4()),
    })
    data.append(new_payment)
    return new_payment

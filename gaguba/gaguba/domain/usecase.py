from gaguba.domain.dto import PaymentCreateDto
from gaguba.domain.entity import Payment


def create_payment(repository, payment: PaymentCreateDto):
    discount = payment.package_price / payment.discount_percentage
    vat = payment.package_price / payment.vat_percentage
    grand_total = sum([
        payment.package_price,
        -discount,
        payment.processing_fee,
        vat
    ])
    new_payment = Payment(**{
        **payment.dict(by_alias=True),
        'id': '',
        'discount': discount,
        'vat': vat,
        'grandTotal': grand_total
    })
    return repository.create(new_payment)


def get_payments(repository):
    return repository.get_all()

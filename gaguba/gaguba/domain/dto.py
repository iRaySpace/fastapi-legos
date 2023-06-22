from pydantic import BaseModel, Field


class PaymentCreateDto(BaseModel):
    package_price: int = Field(alias='packagePrice')
    discount_percentage: int = Field(alias='discountPercentage')
    processing_fee: int = Field(alias='processingFee')
    vat_percentage: int = Field(alias='vatPercentage')

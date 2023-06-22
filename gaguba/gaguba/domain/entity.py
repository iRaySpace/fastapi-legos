from pydantic import BaseModel, Field


class Payment(BaseModel):
    id: str
    package_price: int = Field(alias='packagePrice')
    discount_percentage: int = Field(alias='discountPercentage')
    discount: int
    processing_fee: int = Field(alias='processingFee')
    vat_percentage: int = Field(alias='vatPercentage')
    vat: int
    grand_total: int = Field(alias='grandTotal')

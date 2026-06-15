from pydantic import BaseModel


class PartCreate(BaseModel):
    part_number: str
    description: str
    brand: str | None = None
    cost_price: float
    sell_price: float
    stock_on_hand: int = 0
    bin_location: str | None = None


class PartResponse(PartCreate):
    id: int

    class Config:
        from_attributes = True
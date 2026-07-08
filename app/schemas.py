from pydantic import BaseModel


class PartyCreate(BaseModel):
    party_type: str
    display_name: str
    legal_name: str | None = None

    abn: str | None = None
    website: str | None = None

    contact_name: str | None = None
    phone: str | None = None
    mobile: str | None = None
    email: str | None = None

    address1: str | None = None
    address2: str | None = None
    suburb: str | None = None
    state: str | None = None
    postcode: str | None = None
    country: str | None = None

    credit_limit: float = 0
    balance: float = 0

    status: str = "active"
    notes: str | None = None


class PartyResponse(PartyCreate):
    id: int

    class Config:
        from_attributes = True


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
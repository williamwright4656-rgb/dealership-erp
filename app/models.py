from sqlalchemy import Column, Integer, String, Float
from app.database import Base


class Party(Base):
    __tablename__ = "parties"

    id = Column(Integer, primary_key=True, index=True)

    # Identity
    party_type = Column(String, nullable=False)
    display_name = Column(String, nullable=False, index=True)
    legal_name = Column(String, nullable=True)

    # Business
    abn = Column(String, nullable=True)
    website = Column(String, nullable=True)

    # Contact
    contact_name = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    mobile = Column(String, nullable=True)
    email = Column(String, nullable=True)

    # Address
    address1 = Column(String, nullable=True)
    address2 = Column(String, nullable=True)
    suburb = Column(String, nullable=True)
    state = Column(String, nullable=True)
    postcode = Column(String, nullable=True)
    country = Column(String, nullable=True)

    # Financial
    credit_limit = Column(Float, default=0)
    balance = Column(Float, default=0)

    # General
    status = Column(String, default="active")
    notes = Column(String, nullable=True)


class Part(Base):
    __tablename__ = "parts"

    id = Column(Integer, primary_key=True, index=True)
    part_number = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, nullable=False)
    brand = Column(String, nullable=True)
    cost_price = Column(Float, nullable=False)
    sell_price = Column(Float, nullable=False)
    stock_on_hand = Column(Integer, default=0)
    bin_location = Column(String, nullable=True)
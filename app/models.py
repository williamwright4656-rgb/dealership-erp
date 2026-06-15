from sqlalchemy import Column, Integer, String, Float
from app.database import Base


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
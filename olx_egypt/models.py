from sqlalchemy import Column, Date, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from . import settings

engine = create_engine(settings.DATABSE_URL)
Session = sessionmaker(bind=engine)
session = Session()
DeclarativeBase = declarative_base()


class Olx_Eg(DeclarativeBase):
    """
    Defines the property listing model
    """

    __tablename__ = "olx_egypt"
    _id = Column(Integer, primary_key=True)
    URL = Column("URL", String)
    Breadcrumb = Column("Breadcrumb", String)
    Price = Column("Price", String)
    Title = Column("Title", String)
    Type = Column("Type", String)
    Bedrooms = Column("Bedrooms", String)
    Bathrooms = Column("Bathrooms", String)
    Area = Column("Area", String)
    Location = Column("Location", String)
    Compound = Column("Compound", String)
    seller = Column("seller", String)
    Seller_member_since = Column("Seller_member_since", String)
    Seller_phone_number = Column("Seller_phone_number", String)
    Description = Column("Description", String)
    Amenities = Column("Amenities", String)
    Reference = Column("Reference", String)
    Listed_date = Column("Listed_date", String)
    Level = Column("Level", String)
    Payment_option = Column("Payment_option", String)
    Delivery_term = Column("Delivery_term", String)
    Furnished = Column("Furnished", String)
    Delivery_date = Column("Delivery_date", String)
    Down_payment = Column("Down_payment", String)
    Image_url = Column("Image_url", String)

"""A model containing CarOffer-related modles."""

from typing import Optional

from pydantic import BaseModel, ConfigDict

class CarOfferIn(BaseModel):
    """Model representing Car offer's DTO attributes"""
    registration_number: str
    manufacture: str
    year_of_manufacture: str
    model: str
    type: str
    price_per_day: float
    power: Optional[str] = None
    Usage: Optional[str] = None


class CarOffer(CarOfferIn):
    """Model representing car's attributes in the database."""
    id: int

    model_config = ConfigDict(from_attributes=True, extra="ignore")



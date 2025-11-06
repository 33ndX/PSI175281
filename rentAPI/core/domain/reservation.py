"""A model containing reservation-related modles."""

from typing import Optional

from pydantic import BaseModel, ConfigDict
from datetime import datetime

class ReservationIn(BaseModel):
    """Model representing reservation attributes"""
    user_id: int
    carOffer_id: int
    payment_id: int
    start: datetime
    end: datetime


class Reservation(ReservationIn):
    """Model representing car's attributes in the database."""
    id: int

    model_config = ConfigDict(from_attributes=True, extra="ignore")
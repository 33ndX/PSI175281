"""Modul containing reservation-related domain models."""


from enum import Enum
from pydantic import BaseModel, ConfigDict, UUID4
from datetime import datetime


class ReservationStatus(str, Enum):
    """Status of the reservation."""
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"


class ReservationIn(BaseModel):
    """Model representing reservation's attributes."""
    car_id: int
    user_id: UUID4
    reservation_start: datetime
    reservation_end: datetime
    payment_id: int
    status: ReservationStatus


class Reservation(ReservationIn):
    """Model representing reservation's attributes in the database."""
    id: int

    model_config = ConfigDict(from_attributes=True, extra="ignore")

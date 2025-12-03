"""Modul containing review-related domain models."""

from pydantic import BaseModel, ConfigDict, UUID4


class ReviewIn(BaseModel):
    """Model representing review's attributes."""
    car_id: int
    user_id: UUID4
    body: str


class Review(ReviewIn):
    """Model representing review's attributes in the database."""
    id: int

    model_config = ConfigDict(from_attributes=True, extra="ignore")

"""A module containing DTO models for output reservations."""

from asyncpg import Record  # type: ignore
from pydantic import BaseModel, ConfigDict, UUID4
from datetime import datetime
from rentApi.core.domain.reservation import ReservationStatus
from rentApi.infrastructure.dto.cardto import CarDTO
from rentApi.infrastructure.dto.userdto import UserDTO


class ReservationDTO:
    """A model representing DTO for reservation data."""
    id: int
    car: CarDTO
    reservation_start: datetime
    reservation_end: datetime
    payment: PaymentDTO
    status: ReservationStatus
    user: UserDTO

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
        arbitrary_types_allowed=True
    )

    @classmethod
    def from_record(cls, record: Record) -> "ReservationDTO":
        """A method for preparing DTO instance based on DB record.

        Args:
            record (Record): The DB record.

        Returns:
            CarDTO: The final DTO instance.
        """
        record_dict = dict(record)

        return cls(
            id=record_dict.get("id"),
            car=CarDTO(),
            reservation_start=record_dict.get("reservation_start"),
            reservation_end=record_dict.get("reservation_end"),
            payment=PaymentDTO(),
            status=record_dict.get("status")

        )

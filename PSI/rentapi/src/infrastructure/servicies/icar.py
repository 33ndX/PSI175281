"""Module containing car service abstraction."""

from abc import ABC, abstractmethod
from typing import Iterable

from rentapi.src.core.domain.car import Car
from rentapi.src.infrastructure.dto.cardto import CarDTO


class ICarService(ABC):
    """A class representing car repository."""

    @abstractmethod
    async def get_all(self) -> Iterable[CarDTO]:
        """The method getting all airports from the repository.

        Returns:
            Iterable[AirportDTO]: All airports.
        """

    @abstractmethod
    async def get_by_id(self, car_id: int) -> CarDTO | None:

    @abstractmethod
    async def get_by_model(self, model: str) -> CarDTO | None:
        """The method getting cars assigned to particular model.

        Args:
            model (str): The name of the model.

        Returns:
            CarDTO | None: The car details
        """

    @abstractmethod
    async def get_by_brand(self, brand: str) -> CarDTO | None:
        """The method getting cars assigned to particular brand.

        Args:
            brand (str): The name of the brand.

        Returns:
            CarDTO | None: The car details
        """

    @abstractmethod
    async def delete_car(self, car_id: int) -> bool:
        """The method removing car from the data storage.

        Args:
            car_id (int): The id of the airport.

        Returns:
            bool: Success of the operation.
        """

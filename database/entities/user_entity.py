from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.db import Base


class UserEntity(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int]
    firstname: Mapped[str]
    lastname: Mapped[str]
    age: Mapped[int]
    latitude: Mapped[int]
    longitude: Mapped[int]
    country: Mapped[str]

    bought_products = relationship("BoughtProductEntity", back_populates="user")
    most_bought_categories = relationship("MostBoughtCategoryEntity", back_populates="user")

    def __init__(
            self,
            user_id: int,
            firstname: str,
            lastname: str,
            age: int,
            latitude: float,
            longitude: float,
            country: str,
    ):
        self.user_id = user_id
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.latitude = latitude
        self.longitude = longitude
        self.country = country

    def __str__(self):
        return (
            f"User ID: {self.user_id} -> {self.firstname} {self.lastname} Age: {self.age}"
            f" Cord: {self.latitude}, {self.longitude} -> {self.country}\n"
        )

    def __repr__(self):
        return (
            f"UserEntity(id={self.id}, user_id={self.user_id}, firstname={self.firstname!r}, "
            f"lastname={self.lastname!r}, age={self.age}, latitude={self.latitude}, "
            f"longitude={self.longitude}, country={self.country!r})"
        )

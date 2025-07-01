from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from database.db import Base


class MostBoughtCategoryEntity(Base):
    __tablename__ = "most_bought_categories"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))
    category: Mapped[str]
    total_quantity: Mapped[int]

    user = relationship("UserEntity", back_populates="most_bought_categories")

    def __init__(self, user_id: int, category: str, total_quantity: int):
        self.user_id = user_id
        self.category = category
        self.total_quantity = total_quantity

    def __str__(self):
        return (
            f"{self.id} | User ID: {self.user_id} -> Most bought category: '{self.category}', "
            f"Total quantity: {self.total_quantity} \n"
        )

    def __repr__(self):
        return (
            f"MostBoughtCategoryEntity(id={self.id}, user_id={self.user_id}, "
            f"category='{self.category}', total_quantity={self.total_quantity})"
        )

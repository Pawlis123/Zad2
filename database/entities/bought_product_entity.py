from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from database.db import Base


class BoughtProductEntity(Base):
    __tablename__ = "bought_products"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.product_id"))
    quantity: Mapped[int]

    user = relationship("UserEntity", back_populates="bought_products")
    product = relationship("ProductEntity", back_populates="bought_products")

    def __init__(self, user_id: int, product_id: int, quantity: int):
        self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity

    def __str__(self):
        return (
            f"{self.id} | User with ID: {self.user_id} -> Bought product ID: {self.product_id}, "
            f"Quantity: {self.quantity} \n"
        )

    def __repr__(self):
        return (
            f"BoughtProductEntity(id={self.id}, user_id={self.user_id}, "
            f"product_id={self.product_id}, quantity={self.quantity})"
        )

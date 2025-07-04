from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.db import Base


class CartEntity(Base):
    __tablename__ = "carts"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    cart_id: Mapped[int]
    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.user_id"), nullable=False
    )

    def __init__(self, cart_id: int, user_id: int):
        self.cart_id = cart_id
        self.user_id = user_id

    def __str__(self):
        return f"Cart ID: {self.cart_id} -> User ID: {self.user_id} \n"

    def __repr__(self):
        return (
            f"CartEntity(id={self.id}, cart_id={self.cart_id}, user_id={self.user_id})"
        )

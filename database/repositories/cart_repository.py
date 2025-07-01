from typing import List

from database.db import Session
from database.entities.cart_entity import CartEntity


class CartRepository:
    def __init__(self, session: Session):
        self.session = session

    def save_all_carts(self, carts: list[CartEntity]) -> List[CartEntity]:
        self.session.add_all(carts)
        self.session.commit()
        return carts

    def get_all_carts(self) -> List[CartEntity]:
        return self.session.query(CartEntity).all()

from typing import List

from database.db import Session
from database.entities.bought_product_entity import BoughtProductEntity


class BoughtProductRepository:
    def __init__(self, session: Session):
        self.session = session

    def add_all_bought_products(self, bought_products: list[BoughtProductEntity]) -> List[BoughtProductEntity]:
        self.session.add_all(bought_products)
        self.session.commit()
        return bought_products

    def get_all_bought_products(self) -> List[BoughtProductEntity]:
        return self.session.query(BoughtProductEntity).all()

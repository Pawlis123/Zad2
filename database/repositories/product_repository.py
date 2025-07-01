from typing import List

from database.db import Session
from database.entities.product_entity import ProductEntity


class ProductRepository:
    def __init__(self, session: Session):
        self.session = session

    def save_all_products(self, products: list[ProductEntity]) -> List[ProductEntity]:
        self.session.add_all(products)
        self.session.commit()
        return products

    def get_all_products(self) -> List[ProductEntity]:
        return self.session.query(ProductEntity).all()

from collections import defaultdict
from typing import List

from sqlalchemy import func

from database.db import Session
from database.entities.bought_product_entity import BoughtProductEntity
from database.entities.most_bought_category_entity import MostBoughtCategoryEntity
from database.entities.product_entity import ProductEntity


class MostFrequentlyBoughtRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_and_save_most_frequently_bought_categories_by_user(self) -> List[MostBoughtCategoryEntity]:
        category_totals = (
            self.session.query(
                BoughtProductEntity.user_id,
                ProductEntity.category,
                func.sum(BoughtProductEntity.quantity).label("total_quantity")
            )
            .join(ProductEntity, BoughtProductEntity.product_id == ProductEntity.product_id)
            .group_by(BoughtProductEntity.user_id, ProductEntity.category)
            .all()
        )

        user_top_categories = defaultdict(lambda: ("", 0))

        for user_id, category, total_quantity in category_totals:
            if total_quantity > user_top_categories[user_id][1]:
                user_top_categories[user_id] = (category, total_quantity)

        result = [
            MostBoughtCategoryEntity(user_id=user_id, category=category, total_quantity=total_quantity)
            for user_id, (category, total_quantity) in user_top_categories.items()
        ]

        self.save_most_frequently_bought_categories(result)

        return result

    def save_most_frequently_bought_categories(self, most_frequent_categories_by_user: List[MostBoughtCategoryEntity]):
        self.session.add_all(most_frequent_categories_by_user)
        self.session.commit()

import logging
from typing import List

from database.repositories.bought_product_repository import BoughtProductRepository
from database.repositories.cart_repository import CartRepository
from database.repositories.most_frequently_bought_repository import MostFrequentlyBoughtRepository
from models.Cart import Cart
from utils.mappers.carts_mapper import bought_product_entities_from_carts


class MostBoughtCategoriesService:
    FILE_NAME = "output.txt"

    def __init__(self, bought_product_repository: BoughtProductRepository,
                 cart_repository: CartRepository,
                 most_bought_repository: MostFrequentlyBoughtRepository):
        self.bought_product_repository = bought_product_repository
        self.cart_repository = cart_repository
        self.most_bought_repository = most_bought_repository

    def get_most_bought_categories(self, carts: List[Cart]):
        bought_products_entities = bought_product_entities_from_carts(carts)
        self.bought_product_repository.add_all_bought_products(bought_products_entities)
        result = self.most_bought_repository.get_and_save_most_frequently_bought_categories_by_user()
        self.save_to_file(result)

    def save_to_file(self, data):
        open(f'{self.FILE_NAME}', 'w').close()
        with open(f"{self.FILE_NAME}", "a") as file:
            for item in data:
                file.write(f"{item!s}\n")

        logging.info(f"Output has been saved to {self.FILE_NAME}")

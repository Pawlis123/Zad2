from typing import List

from data_providers.products_data_provider import ProductsDataProvider
from database.repositories.product_repository import ProductRepository
from utils.mappers.products_mapper import product_entities_from_data
from models.Product import Product


class ProductsService:

    def __init__(self, repository: ProductRepository, data_provider: ProductsDataProvider):
        self.repository = repository
        self.data_provider = data_provider

    def get_and_process_all_products(self, batch_size: int) -> List[Product]:
        products = self.data_provider.get_all_products(batch_size)
        product_entities = product_entities_from_data(products)
        self.repository.save_all_products(product_entities)
        return products

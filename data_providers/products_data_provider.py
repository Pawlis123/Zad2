from data_providers import BASE_URL, PRODUCTS_ENDPOINT
from data_providers.data_provider import DataProvider
from utils.mappers.products_mapper import map_products_from_data
from models.Product import Product


class ProductsDataProvider(DataProvider):

    def __init__(self):
        self.PROVIDER_TYPE = 'products'
        self.FILE_NAME = 'products-output.txt'

    def get_url(self, skip: int, limit: int) -> str:
        return f"{BASE_URL}/{PRODUCTS_ENDPOINT}?skip={skip}&limit={limit}"

    def parse_to_objects(self, data_dicts: list[dict]) -> list[Product]:
        return map_products_from_data(data_dicts)

    def get_all_products(self, batch_size: int) -> list[Product]:
        return self.process_all_data(batch_size)

from typing import List

from data_providers import BASE_URL, CARTS_ENDPOINT
from data_providers.data_provider import DataProvider
from utils.mappers.carts_mapper import map_carts_from_data
from models.Cart import Cart


class CartsDataProvider(DataProvider):

    def __init__(self):
        self.PROVIDER_TYPE = 'carts'
        self.FILE_NAME = 'carts-output.txt'

    def parse_to_objects(self, data_dict: list[dict]):
        return map_carts_from_data(data_dict)

    def get_url(self, skip: int, limit: int) -> str:
        return f"{BASE_URL}/{CARTS_ENDPOINT}?skip={skip}&limit={limit}"

    def get_all_carts(self, batch_size: int) -> List[Cart]:
        return self.process_all_data(batch_size)

from typing import List

from data_providers import BASE_URL, USERS_ENDPOINT
from data_providers.data_provider import DataProvider
from utils.mappers.users_mapper import map_users_from_data
from models.User import User


class UsersDataProvider(DataProvider):

    def __init__(self):
        self.PROVIDER_TYPE = 'users'
        self.FILE_NAME = 'users-output.txt'

    def get_url(self, skip: int, limit: int) -> str:
        return f"{BASE_URL}/{USERS_ENDPOINT}?skip={skip}&limit={limit}"

    def parse_to_objects(self, data_dicts: list[dict]) -> list[User]:
        return map_users_from_data(data_dicts)

    def get_all_users(self, batch_size: int) -> List[User]:
        return self.process_all_data(batch_size)

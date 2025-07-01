from typing import List

from data_providers.users_data_provider import UsersDataProvider
from database.repositories.user_repository import UserRepository
from utils.mappers.users_mapper import user_entities_from_data
from models.User import User


class UsersService:

    def __init__(self, repository: UserRepository, data_provider: UsersDataProvider):
        self.repository = repository
        self.data_provider = data_provider

    def get_and_process_all_users(self, batch_size: int) -> List[User]:
        users = self.data_provider.get_all_users(batch_size)
        user_entities = user_entities_from_data(users)
        self.repository.save_all_users(user_entities)
        return users

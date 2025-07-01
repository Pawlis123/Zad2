from typing import List

from data_providers.carts_data_provider import CartsDataProvider
from database.repositories.cart_repository import CartRepository
from utils.mappers.carts_mapper import cart_entities_from_data
from models.Cart import Cart


class CartsService:

    def __init__(self, repository: CartRepository, data_provider: CartsDataProvider):
        self.repository = repository
        self.data_provider = data_provider

    def get_and_process_all_carts(self, batch_size: int) -> List[Cart]:
        carts = self.data_provider.get_all_carts(batch_size)
        cart_entities = cart_entities_from_data(carts)
        self.repository.save_all_carts(cart_entities)
        return carts

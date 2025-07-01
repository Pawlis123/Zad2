from data_providers.carts_data_provider import CartsDataProvider
from data_providers.products_data_provider import ProductsDataProvider
from data_providers.users_data_provider import UsersDataProvider
from database.repositories.bought_product_repository import BoughtProductRepository
from database.repositories.cart_repository import CartRepository
from database.repositories.most_frequently_bought_repository import MostFrequentlyBoughtRepository
from database.repositories.product_repository import ProductRepository
from database.repositories.user_repository import UserRepository
from services.carts_service import CartsService
from services.most_bought_categories_service import MostBoughtCategoriesService
from services.products_service import ProductsService
from services.users_service import UsersService


def get_carts_service(session):
    repository = CartRepository(session)
    carts_data_provider = CartsDataProvider()
    return CartsService(repository, carts_data_provider)


def get_products_service(session):
    repository = ProductRepository(session)
    products_data_provider = ProductsDataProvider()
    return ProductsService(repository, products_data_provider)


def get_user_service(session):
    repository = UserRepository(session)
    products_data_provider = UsersDataProvider()
    return UsersService(repository, products_data_provider)


def get_most_bought_categories_service(session):
    bought_product_repository = BoughtProductRepository(session)
    cart_repository = CartRepository(session)
    most_bought_repository = MostFrequentlyBoughtRepository(session)
    return MostBoughtCategoriesService(bought_product_repository, cart_repository, most_bought_repository)

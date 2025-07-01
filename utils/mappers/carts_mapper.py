from itertools import chain
from typing import List

from database.entities.bought_product_entity import BoughtProductEntity
from database.entities.cart_entity import CartEntity
from models.Cart import Cart


def cart_from_data(cart: dict) -> Cart:
    return Cart(cart["id"], cart["userId"], {product["id"]: product["quantity"] for product in cart["products"]})


def map_carts_from_data(carts_data: list[dict]) -> list[Cart]:
    return list(map(
        lambda cart: cart_from_data(cart),
        carts_data
    ))


def map_cart_to_bought_products_entities(cart: Cart) -> list:
    return list(map(lambda item: BoughtProductEntity(cart.user_id, item[0], item[1]), cart.products.items()))


def cart_entity_from_data(cart: Cart) -> CartEntity:
    return CartEntity(cart.cart_id, cart.user_id)


def cart_entities_from_data(carts: list[Cart]) -> List[CartEntity]:
    return list(map(
        lambda cart: cart_entity_from_data(cart),
        carts
    ))


def bought_product_entities_from_carts(carts: list[Cart]) -> List[CartEntity]:
    return list(chain.from_iterable(map(
        lambda cart: list(map(
            lambda item: BoughtProductEntity(cart.user_id, item[0], item[1]),
            cart.products.items()
        )),
        carts
    )))

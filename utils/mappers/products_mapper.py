from typing import List

from database.entities.product_entity import ProductEntity
from models.Product import Product


def product_from_data(product: dict) -> Product:
    return Product(
        product["id"],
        product["title"],
        product["price"],
        product["category"]
    )


def product_to_entity(product: Product) -> ProductEntity:
    return ProductEntity(
        product.product_id,
        product.title,
        product.price,
        product.category,
    )


def map_products_from_data(products_data: list[dict]) -> list[Product]:
    return list(map(
        lambda product: product_from_data(product),
        products_data
    ))


def product_entities_from_data(products: list[Product]) -> List[ProductEntity]:
    return list(map(
        lambda product: product_to_entity(product),
        products
    ))

from typing import List

from database.entities.user_entity import UserEntity
from models.User import User


def user_from_data(user: dict) -> User:
    return User(
        user["id"],
        user["firstName"],
        user["lastName"],
        user["age"],
        user["address"]["coordinates"]["lat"],
        user["address"]["coordinates"]["lng"],
    )


def map_users_from_data(users_data: list[dict]) -> list[User]:
    return list(map(
        lambda user: user_from_data(user),
        users_data
    ))


def user_entity_from_data(user: User) -> UserEntity:
    return UserEntity(
        user.user_id,
        user.first_name,
        user.last_name,
        user.age,
        user.latitude,
        user.longitude,
        user.country
    )


def user_entities_from_data(users: list[User]) -> List[UserEntity]:
    return list(map(
        lambda user: user_entity_from_data(user),
        users
    ))

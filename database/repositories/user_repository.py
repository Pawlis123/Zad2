from typing import List

from database.db import Session
from database.entities.user_entity import UserEntity


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def save_all_users(self, users: list[UserEntity]) -> List[UserEntity]:
        self.session.add_all(users)
        self.session.commit()
        return users

    def get_all_users(self) -> List[UserEntity]:
        return self.session.query(UserEntity).all()

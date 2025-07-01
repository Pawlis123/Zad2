from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
import logging

from database.db import Base, db, Session
from utils.service_managers import get_carts_service, get_products_service, get_user_service, \
    get_most_bought_categories_service

batch_size = 50
Base.metadata.create_all(db)
session = Session()
carts_service = get_carts_service(session)
products_service = get_products_service(session)
users_service = get_user_service(session)
most_bought_categories_service = get_most_bought_categories_service(session)
app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    users_service.get_and_process_all_users(batch_size)
    products_service.get_and_process_all_products(batch_size)
    carts = carts_service.get_and_process_all_carts(batch_size)
    most_bought_categories_service.get_most_bought_categories(carts)
    yield


app = FastAPI(lifespan=lifespan)

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    uvicorn.run(app, host="0.0.0.0", port=8000)

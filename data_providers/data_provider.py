from abc import ABC, abstractmethod
from itertools import takewhile, count, chain
from typing import Any, Dict, Optional, List

import requests
import logging

from database.db import Session


class DataProvider(ABC):
    PROVIDER_TYPE: str
    FILE_NAME: str
    session: Session

    @abstractmethod
    def get_url(self, skip: int, limit: int) -> str:
        pass

    @abstractmethod
    def parse_to_objects(self, data_dicts: list[dict]):
        pass

    def get_data(self, skip: int, limit: int):
        url = self.get_url(skip, limit)
        response = requests.get(url)

        if response.status_code == 200:
            logging.info(f"FETCHED DATA: {self.__class__.__name__.capitalize()}")
            return response.json()
        else:
            logging.error(f"DATA FETCH FAILED: {self.__class__.__name__.capitalize()}")

    def fetch_batch(self, skip: int, batch_size: int) -> Optional[dict[str, Any]]:
        try:
            data = self.get_data(skip, batch_size)
            if data and self.PROVIDER_TYPE in data:
                logging.info(f"Range: {skip} - {skip + batch_size}")
                return data
        except Exception as e:
            logging.error(f"Error fetching data for range {skip} - {skip + batch_size}: {e}")
        return None

    def process_batch(self, data: Dict[str, Any]) -> list[Any]:
        data_type = data[self.PROVIDER_TYPE]
        return self.parse_to_objects(data_type)

    def safe_process_batch(self, batch: Optional[Dict[str, Any]]) -> list[Any]:
        if batch:
            return self.process_batch(batch)
        return []

    def process_all_data(self, batch_size: int) -> list[Any]:
        initial = self.fetch_batch(0, batch_size)
        if not initial or "total" not in initial:
            return []

        total = initial["total"]
        initial_processed = self.process_batch(initial)

        skips = takewhile(lambda s: s < total, count(batch_size, batch_size))
        batches = map(lambda skip: self.fetch_batch(skip, batch_size), skips)
        processed_batches = map(self.safe_process_batch, batches)

        return initial_processed + list(chain.from_iterable(processed_batches))

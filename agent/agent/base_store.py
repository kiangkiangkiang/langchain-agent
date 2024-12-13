from abc import ABC, abstractmethod
from collections import defaultdict

STORE_ITEMS = defaultdict(dict)


def registry_items(store_name: str, items_name: str):
    def decorator(func):
        if items_name in STORE_ITEMS[store_name]:
            raise ValueError(f"This items name {items_name} is already exist.")
        else:
            STORE_ITEMS[store_name][items_name] = func

        return func

    return decorator


class BaseStore(ABC):
    @staticmethod
    def list_store():
        return STORE_ITEMS

    @classmethod
    def search(cls, items_name: str):
        if items_name not in STORE_ITEMS[cls.store_name]:
            return None
        else:
            return STORE_ITEMS[cls.store_name][items_name]()

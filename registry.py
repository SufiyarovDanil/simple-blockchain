import os
import json
from coin_block import CoinBlock, GENESIS_HASH


REGISTRY_PATH: str = 'registry.json'


def __is_registry_existing() -> bool:
    return os.path.exists(REGISTRY_PATH)


def __create_registry() -> None:
    with open(REGISTRY_PATH, 'w', encoding='utf-8') as file:
        json.dump({'blocks': []}, file, indent=4, ensure_ascii=False)
        file.close()


def __get_hash_of_last_block() -> str:
    with open(REGISTRY_PATH, 'r', encoding='utf-8') as file:
        return json.load(file)['blocks'][-1]['hash']


def add_transactions_to_registry(transaction_data: list[str]) -> None:
    if not __is_registry_existing():
        __create_registry()
    
    with open(REGISTRY_PATH, 'r', encoding='utf-8') as file:
        json_data = json.load(file)
        prev_hash: str = GENESIS_HASH if len(json_data['blocks']) == 0 else __get_hash_of_last_block()
        new_block: CoinBlock = CoinBlock(prev_hash, transaction_data)
        file.close()

    with open(REGISTRY_PATH, 'w', encoding='utf-8') as file:
        json_data['blocks'].append(new_block.as_dict())
        json.dump(json_data, file, indent=4, ensure_ascii=False)
        file.close()

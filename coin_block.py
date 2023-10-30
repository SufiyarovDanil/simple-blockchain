from hashlib import sha256


GENESIS_HASH: str = '000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f'


class CoinBlock:
    __data: list[str]
    __hash: str

    def __init__(self, prev_block_hash: str, transactions: list[str]):
        self.__data =  transactions.copy()
        self.__hash = sha256((''.join(self.__data) + prev_block_hash).encode()).hexdigest()
    
    def as_dict(self):
        return {
            'data': self.__data,
            'hash': self.__hash
        }
    
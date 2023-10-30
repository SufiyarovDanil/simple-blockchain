from registry import add_transactions_to_registry


if __name__ == '__main__':
    transactions: list[str] = list()

    print('Вводите транзакции: (для прекращения ввода напишите __end__)')

    while True:
        data: str = input('>>> ')

        if data == '__end__':
            break

        transactions.append(data)

    add_transactions_to_registry(transactions)

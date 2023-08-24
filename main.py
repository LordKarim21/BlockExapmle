import requests
import base64


def get_transactions_from_block(number: int) -> list:
    url = f"your_url"

    try:
        response = requests.get(url)
        print(response.status_code)
        data = response.json()
        transactions = []
        if 'data' in data and 'txs' in data['data']:
            txs_base64 = data['data']['txs']
            for tx_base64 in txs_base64:
                tx_bytes = base64.b64decode(tx_base64)
                transactions.append(tx_bytes.decode('utf-8'))
        return transactions
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return []


block_number = 11260637  # your number
transactions = get_transactions_from_block(block_number)

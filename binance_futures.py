import logging
import requests
import pprint

logger = logging.getLogger()


def get_contracts():
    response_object = requests.get("https://api.binance.com/api/v3/exchangeInfo")
    print(response_object.status_code)

    contracts = []

    for contract in response_object.json()['symbols']:
        contracts.append(contract['symbol'])

    return contracts


print(get_contracts())

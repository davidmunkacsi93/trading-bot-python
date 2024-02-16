import logging
import requests

logger = logging.getLogger()


def get_contracts():
    base_uri = "https://testnet.bitmex.com/api/v1"

    response_object = requests.get(f"{base_uri}/instrument/active")

    contracts = []

    for contract in response_object.json():
        contracts.append(contract['symbol'])

    return contracts

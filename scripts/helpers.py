from brownie import accounts, config, network
from web3 import Web3

FORK_BLOCKCHAIN_ENVIRONMENTS = ["mainnet-fork-dev", "mainnet-fork"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

DECIMALS = 8
STARTING_PRICE = 200000000000


def get_account():
    active_network = network.show_active()
    if active_network in LOCAL_BLOCKCHAIN_ENVIRONMENTS or active_network in FORK_BLOCKCHAIN_ENVIRONMENTS:
        account = accounts[0]
    else:
        account = accounts.add(config["wallets"]["from_key"])
    print(f"retrieved {active_network} account: {account}")
    return account


def deploy_mock(_contract, _account):
    print(type(_contract))
    print(f"Deploying mock: {_contract}")
    if len(_contract) <= 0:
        _contract.deploy(DECIMALS, STARTING_PRICE, {"from": _account})
    print("Mocks deployed!")
    return _contract[-1].address

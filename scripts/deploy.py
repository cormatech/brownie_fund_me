from brownie import FundMe, MockV3Aggregator, config, network
from web3 import Web3

from scripts.helpers import deploy_mock, get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS

def deploy_fund_me():
    account = get_account()
    active_network = network.show_active()
    print(f"the active network is {active_network}")
    if active_network not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][active_network]["eth_usd_price_feed"]
    else:
        price_feed_address = deploy_mock(MockV3Aggregator, account)

    
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"].get(active_network).get("verify"),
    )
    print(f"Contract deployed: {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()

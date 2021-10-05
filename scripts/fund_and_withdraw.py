from brownie import FundMe

from scripts.helpers import get_account


def fund():
    # retrieve latest deployed FundMe contract on network
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(f"The current entrance fee is {entrance_fee}")
    print("Funding")
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    # retrieve latest deployed FundMe contract on network
    fund_me = FundMe[-1]
    account = get_account()
    print(f"Withdrawing {fund_me.balance()}")
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()

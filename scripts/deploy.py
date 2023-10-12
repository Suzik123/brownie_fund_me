from brownie import FundMe,MockV3Aggregator, accounts, config, network
from scripts.helpful_scripts import *
from web3 import Web3
def deploy_fund_me():
    account = get_account()
    price_feed_address = deploy_mocks()    

    fund_me = FundMe.deploy(price_feed_address, {"from": account})
    return fund_me

def main():
    deploy_fund_me()
from brownie import accounts, network, config, MockV3Aggregator
from web3 import Web3
FORK_LOCAL_INVIRONMENTS = ["mainnet-fork"]
LOCAL_BLOCKCHAIN_ENVIROMENTS = ['development', 'ganache-local']
def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIROMENTS or network.show_active() in FORK_LOCAL_INVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIROMENTS:
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"] #"0xD4a33860578De61DBAbDc8BFdb98FD742fA7028e"
    else:
        if len(MockV3Aggregator) <=0:
            mock_aggregator = MockV3Aggregator.deploy(18, Web3.toWei(2000, "ether"), {"from": get_account()})
        price_feed_address = MockV3Aggregator[-1].address
    return price_feed_address
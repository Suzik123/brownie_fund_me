from scripts.helpful_scripts import *
from scripts.deploy import deploy_fund_me
from brownie import network, exceptions
import pytest
def test_can_fund_and_withdraw():
    print('x')
    account = get_account()
    fund_me = deploy_fund_me()
    entrance_fee = fund_me.getEntranceFee()
    tx = fund_me.fund({"from":account, "value":entrance_fee})
    
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee

    txx = fund_me.withdraw({"from":account})
    
    assert fund_me.addressToAmountFunded(account.address) == 0

def test_only_owner_can_withdraw():
    if network.show_active not in ['development', 'ganache-local']:
        pytest.skip("only for local testing")
    account = get_account()
    fund_me = deploy_fund_me()
    bad_actor = accounts.add()
   
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from":bad_actor})
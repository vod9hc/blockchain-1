#### Smart Contracts ####
import os
import json

from dotenv import load_dotenv
from web3 import Web3

load_dotenv()
infura_url = os.getenv('endpoint')

w3 = Web3(Web3.HTTPProvider(infura_url))
print(w3.isConnected())

abi = json.loads(os.getenv('abi'))
address = os.getenv('address')

contracts = w3.eth.contract(address=address, abi=abi)

print(contracts)
totalSup = contracts.functions.totalSupply().call()
print(w3.fromWei(totalSup, 'ether'))
print(contracts.functions.name().call())
print(contracts.functions.symbol().call())
balance = contracts.functions.balanceOf(address).call()
print(w3.fromWei(balance, 'ether'))


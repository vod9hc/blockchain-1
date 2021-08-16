#### Introduction ####
import os

from dotenv import load_dotenv
from web3 import Web3

load_dotenv()
infura_url = os.getenv('endpoint')
add_wallet = os.getenv('address_wl')

#Define var to connect Server
w3 = Web3(Web3.HTTPProvider(infura_url))
w3.isConnected()

#Get latest block number
print(w3.eth.blockNumber)
#Get block
print(w3.eth.get_block('latest'))
#Get balance from Wallet
balance = w3.eth.getBalance(add_wallet)
print(w3.fromWei(balance, "ether"))
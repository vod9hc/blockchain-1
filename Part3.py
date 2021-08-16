#How to send a cryptocurrency om Ethereum
import os

from dotenv import load_dotenv
from web3 import Web3

load_dotenv()
acc_1 = os.getenv('acc_1')
acc_2 = os.getenv('acc_2')
privatek_1 = os.getenv('private_key_1')
ganache_url = os.getenv('ganache_url')

w3 = Web3(Web3.HTTPProvider(ganache_url))
print(w3.isConnected())

#get a nonce
nonce = w3.eth.getTransactionCount(acc_1)
#build a transaction
tx = {
    'nonce': nonce,
    'to': acc_2,
    'value': w3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': w3.toWei('50', 'gwei')
}
#sign transaction
signed_tx = w3.eth.account.signTransaction(tx, privatek_1)
#send transaction
tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
#get transaction hash
print(w3.toHex(tx_hash))


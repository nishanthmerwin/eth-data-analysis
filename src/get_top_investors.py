#!/usr/bin/env python


from web3 import Web3, HTTPProvider
import json
from tqdm import tqdm

web3 = Web3(HTTPProvider('https://mainnet.infura.io/hackit'))

with open("../data/bunny_wallets.json") as fp:
    bunny_wallets = json.load(fp)

bunny_wallets = sorted(bunny_wallets, key=lambda x:x['balance'])[::-1][:1000]

with open("../data/bat_wallets.json") as fp:
    bat_wallets = json.load(fp)
bat_wallets = sorted(bat_wallets, key=lambda x:x['balance'])[::-1][:1000]

for wallet in tqdm(bunny_wallets + bat_wallets):
    addr = wallet['wallet']
    wallet['eth_balance'] = web3.eth.getBalance(addr) / 1e18


print sum([x['eth_balance'] for x in bunny_wallets])
print sum([x['eth_balance'] for x in bat_wallets])









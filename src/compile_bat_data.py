#!/usr/bin/env python

import json
import os
from os.path import join
from tqdm import tqdm 


txn_dir = "../data/bat_txns"
txn_files = os.listdir(txn_dir)

all_txns = []
for txn_file in tqdm(txn_files):
    path = join(txn_dir, txn_file)
    with open(path) as fp:
        txns = json.load(fp)
    all_txns += txns

wallet_map = {}
for txn in tqdm(all_txns):
    from_wallet = txn['returnValues']['_from']
    to_wallet = txn['returnValues']['_to']
    txn['from'] = from_wallet
    txn['to'] = to_wallet
    txn['value'] = int(txn['returnValues']['_value'])
    txn_compiled = {"from":txn['from'], "to":txn['to'],"value":txn['value'],\
            "block":txn['blockNumber']}
    try:
        wallet_map[from_wallet].append(txn_compiled)
    except KeyError:
        wallet_map[from_wallet] = [txn_compiled]

    try:
        wallet_map[to_wallet].append(txn_compiled)
    except KeyError:
        wallet_map[to_wallet] = [txn_compiled]

all_wallets = []
for wallet, txns in tqdm(wallet_map.iteritems(), total=len(wallet_map)):

    outputs = [x for x in txns if x['from'] == wallet]
    inputs = [x for x in txns if x['to'] == wallet]

    total_in = sum([x['value'] for x in inputs])
    total_out = sum([x['value'] for x in outputs])
    balance = total_in - total_out
    balance = balance / 1000000000000000000.0
    wallet_dict = dict(inputs=inputs, outputs=outputs, balance=balance, wallet=wallet)
    all_wallets.append(wallet_dict)

all_wallets = sorted(all_wallets, key=lambda x:x['balance'])[::-1]

with open("../data/bat_wallets.json", "w") as fp:
    json.dump(all_wallets, fp)






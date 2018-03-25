#!/usr/bin/env python

import json
from tqdm import tqdm


with open("../data/bat_wallets.json") as fp:
    wallets = json.load(fp)

all_txns = []
all_blocks = []

print len(wallets)
wallets = [x for x in wallets if not x['balance'] < 0]
print len(wallets)


for wallet in tqdm(wallets):
    inputs = wallet['inputs']
    outputs = wallet['outputs']
    txns = inputs + outputs
    all_txns += txns

for txn in tqdm(all_txns):
    block = txn['block']
    all_blocks.append(block)

latest = max(all_blocks)
earliest = min(all_blocks)
bin_sizes = (latest - earliest) * 0.2
bin_mins = [dict(i=i,min_val=earliest + (i*bin_sizes)) for i in xrange(5)]

def get_quartile(block, bin_mins):
    matched_quartile = None
    for i in xrange(len(bin_mins)):
        binmin = bin_mins[i]['min_val']
        if block >= binmin:
            matched_quartile = i
        else:
            break
    return matched_quartile

for txn in tqdm(all_txns):
    block = txn['block']
    quartile = get_quartile(block, bin_mins)
    txn['bin'] = quartile


for wallet in wallets:
    for bin_idx in xrange(5):
        inputs = [x['value'] for x in wallet['inputs'] if x['bin'] <= bin_idx]
        outputs = [x['value'] for x in wallet['outputs'] if x['bin'] <= bin_idx]
        bin_balance = sum(inputs) - sum(outputs)
        bin_balance = bin_balance / 1000000000000000000.0
        wallet['balance_{}'.format(bin_idx)] = bin_balance

max_radius = 12
all_nodes = []
for bin_idx in xrange(5):
    balance_key = "balance_{}".format(bin_idx)
    bin_wallets = [x for x in wallets if\
            x[balance_key] > 0]
    total_value = float(sum([x[balance_key] for x in bin_wallets]))

    print bin_idx, total_value, len(bin_wallets)

    for wallet in bin_wallets:
        balance = wallet['balance_{}'.format(bin_idx)]
        rel_value = balance / total_value
        radius = rel_value * max_radius
        node = dict(rel_value=rel_value, radius=radius, bin_idx=bin_idx)
        all_nodes.append(node)


import random
random.shuffle(all_nodes)

all_nodes = sorted(all_nodes, key=lambda x:x['rel_value'])[::-1][:20000]


with open("./bat_nodes.json", "w") as fp:
    json.dump(all_nodes, fp)










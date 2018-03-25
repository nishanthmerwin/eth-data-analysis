#!/usr/bin/env python

import json
import os
from os.path import join
from nmutils import generalutils
from tqdm import tqdm
import time


start = 3788558
latest = 5315040 
outdir = "../data/bat_txns"

all_blocks = list(xrange(start,latest))

chunked_blocks = list(generalutils.chunks(all_blocks, 100))

all_blocks = []
i=0
for chunk in tqdm(chunked_blocks):
    i += 1
    min_block = min(chunk)
    max_block = max(chunk)
    outpath = join(outdir, "{}.json".format(i))
    all_blocks.append(dict(min_block=min_block,\
            max_block=max_block, outpath=outpath))

print len(all_blocks)

all_blocks = [x for x in all_blocks if not os.path.exists(x['outpath'])]

for block in tqdm(all_blocks):
    min_block = block['min_block']
    max_block = block['max_block']
    outpath = block['outpath']
    os.system("node ./make_bat_calls.js {} {} {}"\
            .format(min_block, max_block, outpath))
    time.sleep(1)




#!/usr/bin/env python

import json
import os
from os.path import join
from nmutils import generalutils
from tqdm import tqdm


start = 3788558
latest = 5315040 
outdir = "../data/bat_txns"

all_blocks = list(xrange(start,latest))

chunked_blocks = list(generalutils.chunks(all_blocks, 100))

i=0
for chunk in tqdm(chunked_blocks):
    i += 1
    min_block = min(chunk)
    max_block = max(chunk)
    outpath = join(outdir, "{}.json".format(i))
    if os.path.exists(outpath):
        continue
    os.system("node ./make_bat_calls.js {} {} {}"\
            .format(min_block, max_block, outpath))


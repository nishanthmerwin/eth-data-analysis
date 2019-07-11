

import random
import json

with open("./bat_nodes.json") as fp:
    nodes = json.load(fp)

nodes = sorted(nodes, key=lambda x:x['rel_value'])[::-1]

nodes = nodes[:2000]

with open("./bat_nodes_sampled.json", "w") as fp:
    json.dump(nodes, fp)

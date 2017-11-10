import csv
from itertools import permutations

import networkx as nx


def hex_distance(a, b):
    return (abs(a['q'] - b['q']) 
          + abs(a['q'] + a['r'] - b['q'] - b['r'])
          + abs(a['r'] - b['r'])) / 2


def get_minutes(a, b, fspeed, data):
    d = hex_distance(data[a], data[b])
    speed = (fspeed + data[b]['boost']) / 60.0
    return d / speed 
    

# read transport network data from file
with open('transport.csv') as csvfile:
     reader = csv.DictReader(csvfile)
     data = [row for row in reader]

# convert string data to int for math usage
for row in data:
    row['q'] = int(row['q'])
    row['r'] = int(row['r'])
    row['boost'] = int(row['boost'])

# convert data to dict
new_data = {}
for row in data:
    new_data[row['station']] = row
data = new_data

# build network
links = [(start, end)
         for start, end in
         permutations(data.keys(), 2)]

FSPEED = 6
links = [(start, end, get_minutes(start, end, FSPEED, data))
         for start, end in links]
print(links)

tnet = nx.DiGraph()
tnet.add_weighted_edges_from(links)
print(nx.dijkstra_path(tnet, 'P', 'T'))

import csv
from itertools import permutations

import networkx as nx


def hex_distance(a, b):
    return (abs(a['q'] - b['q']) 
          + abs(a['q'] + a['r'] - b['q'] - b['r'])
          + abs(a['r'] - b['r'])) / 2


def get_minutes(a, b, fspeed, data):
    # prevent movement from other to other by increasing weight to a massive number
    if data[a]['owner'] == 'other' and data[b]['owner'] == 'other':
        return 99999999
    d = hex_distance(data[a], data[b])
    speed = (fspeed + data[b]['boost']) / 60.0
    return d / speed 
    

def build_network(path, fspeed):
    # read transport network data from file
    with open(path) as csvfile:
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
    # start and end are station name strings
    links = [(start, end)
             for start, end in
             permutations(data.keys(), 2)]

    links = [(start, end, get_minutes(start, end, fspeed, data))
             for start, end in links]

    tnet = nx.DiGraph()
    # DiGraph.add_weighted_edges_from(ebunch, weight='weight', **attr)
    # Add all the edges in ebunch as weighted edges with specified weights.
    tnet.add_weighted_edges_from(links)
    return tnet


import networkx as nx
import matplotlib.pyplot as plt
import json
import math
import sys

def main():
    print('start graphmaker');

    currencygraph = graphmaker('pairlist.json','baselist.json');
    
    for node in currencygraph.neighbors('NU'):
        print(node)
        print(currencygraph.get_edge_data('BTC','NU'));

    print('end graphmaker');


def graphmaker(edgefile, nodefile):
    G = nx.MultiDiGraph();

    with open(nodefile) as file:
        data = json.load(file);

        for ticker in data:
            G.add_node(ticker);

    with open(edgefile) as file:
        data = json.load(file);

        for orderbook in data:
            pair = orderbook[0].split('-'); #split ticker after '-' character, example BTC-EUR =[BTC,EUR]
            
            bid_currency = pair[0] #basecurrency in bids -> start of edge, quotecurrency in asks -> end of edge
            ask_currency = pair[1] #basecurrency in asks -> start of edge, quotecurrency in bids -> end of edge

            for bid in orderbook[1]['bids']:
                orderprice = 1/float(bid[0]); #1/price = convertable amount from endnode back to startnode / "best price willing to buy" at startnode
                ordersize = float(bid[1])*float(bid[0]); # size of order converted to basecurrency => conversionrate*amount
                G.add_edge(ask_currency,bid_currency,weight=orderprice,size=ordersize); #Edge from EUR --> BTC 
            
            for ask in orderbook[1]['asks']:
                orderprice = ask[0]; #seller willing to sell at endnode
                ordersize = ask[1]; #amount seller willing to sell
                G.add_edge(bid_currency,ask_currency,weight=orderprice,size=ordersize); #Edge from BTC --> EUR


    file.close();
    return G;
        
                






main();
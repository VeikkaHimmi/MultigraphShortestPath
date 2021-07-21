import json
import requests
import cbpro

#---------------------------------------------------------------#
# getCurrencyPairs() extracts exhange rates between currencies
# exhangerate API only provides snapshot of current rates, buy/sell amount
# on a rate could be used to create an Maxinum flow problem between
# currencies, where the buy/sell amount presents maxinum flow on one rate(or edge)
# -> multiple edges between currencies
#---------------------------------------------------------------#
def getCurrencyPairs():
    
    print("start getCurrencyPairs");

    tickers = tickersFromFile(); #extracts used currency tickers from json.file

    client = cbpro.PublicClient();
    pairlist = [];

    for ticker in tickers: #extracts rates between tickers from exhangerate API
        pair = [];
        pair.append(ticker);
        orderbook = client.get_product_order_book(ticker,level=2); # change level = 3 for whole orderbook, level = 2 -> 50 best orders
        pair.append(orderbook);

        pairlist.append(pair);

    print(pairlist[3]);
        
    saveToFile('pairlist.json',pairlist);
    
    print("stop getCurrencyPairs");

    
def saveToFile(file,data):
    
    with open(file,'w') as outfile:
        
        json.dump(data,outfile);


def tickersFromFile():

    with open ('currencylist.json') as file:
        data = json.load(file);
        
    return data;

getCurrencyPairs();
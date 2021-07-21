import json
import requests
import cbpro

#---------------------------------------------------------------#
# getCurrencyLabels() extracts available tickers from API and saves
# them to currencylist.json
#---------------------------------------------------------------#
def getCurrencyLabels():
    print("Start getCurrencies");
    
    public_client = cbpro.PublicClient();
    data = public_client.get_products();
    pairlist = [];
    base_currencylist = [];
    quote_currencylist = [];

    for pair in data:
        base_currency = pair["base_currency"];
        quote_currency = pair["quote_currency"];
        
        if ((base_currency +"-"+quote_currency) or (quote_currency+"-"+base_currency)) in pairlist:
            continue;

        pairlist.append(pair["id"])
        base_currencylist.append(pair["base_currency"]);
        quote_currencylist.append(pair["quote_currency"]);
    
    base_currencylist = base_currencylist+quote_currencylist;
    base_currencylist = list(dict.fromkeys(base_currencylist));

    #printList(pairlist,base_currencylist);
    
    saveToFile('currencylist.json',pairlist); #function for saving tickers as json file
    saveToFile('baselist.json',base_currencylist);

    print("Done getCurrencies");

def printList(pairlist,base_currencylist):
    print(pairlist);
    print(len(pairlist));
    print("----------------------------------------");
    print(base_currencylist);
    print("amount: "+str(len(base_currencylist)));

def saveToFile(file,data):

    with open(file,'w') as outfile:
        json.dump(data,outfile);

getCurrencyLabels();
    

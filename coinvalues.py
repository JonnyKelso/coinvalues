#! /usr/bin/env python3

import requests
import time
from datetime import datetime

# *** from https://coinmarketcap.com/api/
# Misc
#    All 'last_updated' fields are unix timestamps.
# Limits
#    Please limit requests to no more than 10 per minute.
#    Endpoints update every 5 minutes.

BITCOIN_API_URL = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
ETHEREUM_API_URL = 'https://api.coinmarketcap.com/v1/ticker/ethereum/'
POLL_PERIOD = 5 * 60 # 5 minutes
DEV_PERIOD = 10

def get_latest_price(coin_url):
    response = requests.get(coin_url, "convert=GBP")
    response_json = response.json()

    #print(*response_json, sep='\n')

    # Convert the price to a floating point number
    return float(response_json[0]['price_gbp'])

def main():
    btc_history = []
    eth_histroy = []
    outfile = open("btc_history.txt", 'a')
    while True:
        btc_price = get_latest_price(BITCOIN_API_URL)
        eth_price = get_latest_price(ETHEREUM_API_URL)
        date = datetime.now()
#        btc_history.append({'date': date, 'price': price})

        print('date:' + str(date) + 
                ' btc:' + str(btc_price) + 'gbp, ' +
                ' eth:' + str(eth_price) + 'gbp')

        outfile.write(str(date) + ',' + str(btc_price) + ',' + str(eth_price) + '\n')

        time.sleep(DEV_PERIOD) #POLL_PERIOD)


if __name__ == '__main__':
    main()


import json
import os
from time import sleep
from dotenv import load_dotenv
from binance import Client, AsyncClient, ThreadedWebsocketManager, ThreadedDepthCacheManager

load_dotenv()
api_key = os.getenv('biapi_key')
api_sec = os.getenv('bisec_key')
tapi_key = os.getenv('tapi_key')
tapi_sec = os.getenv('tapi_sec')
turl_testner = os.getenv('url_testnet')
client = Client(tapi_key, tapi_sec)
tickers = client.get_ticker()
print(json.dumps(tickers, indent=2))
#client.API_URL = turl_testner

def main():
    btc_price = {'BTCUSDT': None, 'error': False}

    def btc_trade_history(msg):
        if msg['e'] != 'error':
            btc_price['BTCUSDT'] = float(msg['c'])
        else:
            btc_price['error'] = True

    # init and start the websocket
    twm = ThreadedWebsocketManager()
    twm.start()
    #subcribe to a stream
    twm.start_symbol_ticker_socket(symbol='BTCUSDT', callback=btc_trade_history)
    while not btc_price['BTCUSDT']:
        sleep(0.1)
    while True:
        if btc_price['error']:
            twm.stop()
            sleep(2)
            twm.start()
            btc_price['error'] = False
        else:
            if btc_price['BTCUSDT'] > 50000:
                try:
                    print('hello')
                except Exception as e:
                    print(e)
        sleep(0.1)

    twm.stop()

if __name__ == '__main__':
    main()
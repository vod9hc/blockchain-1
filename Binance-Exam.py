import json
import os
from time import sleep
from dotenv import load_dotenv
from binance import Client, AsyncClient, ThreadedWebsocketManager, ThreadedDepthCacheManager

load_dotenv()
api_key = os.getenv('biapi_key')
api_sec = os.getenv('bisec_key')
turl_testner = os.getenv('url_testnet')
client = Client(api_key, api_sec)
#client.API_URL = turl_testner

def main():
    tickers = client.get_ticker()
    print(json.dumps(tickers, indent=2))

if __name__ == '__main__':
    main()
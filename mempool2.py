import asyncio
import json

from web3 import Web3
# from web3.middleware import geth_poa_middleware # only needed for PoA networks like BSC
import requests
from websockets import connect
from eth_abi import decode_single, decode_abi

# adapter = requests.sessions.HTTPAdapter(pool_connections=50000, pool_maxsize=50000) # pool connections and max size are for HTTP calls only, since we are using WS they are not needed. 
session = requests.Session()
w3 = Web3(Web3.WebsocketProvider("wss://mainnet.infura.io/ws/v3/43b2d6f15d164cb4bbe4d4789831f242"))
# w3.middleware_onion.inject(geth_poa_middleware, layer=0) # only needed for PoA networks like BSC


async def get_event():
    async with connect("wss://mainnet.infura.io/ws/v3/43b2d6f15d164cb4bbe4d4789831f242") as ws:
        await ws.send(json.dumps({"id": 1, "method": "eth_subscribe", "params":  ["newPendingTransactions"]}))
        subscription_response = await ws.recv()
        print(subscription_response)
        while True:
            try:
                message = await asyncio.wait_for(ws.recv(), timeout=60)
                # decoded = decode_single('(uint112,uint112)',bytearray.fromhex(json.loads(message)['params']['result']['data'][2:]))
                # print(list(decoded))
                print(message)
                pass
            except:
                pass
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    while True:
        loop.run_until_complete(get_event())
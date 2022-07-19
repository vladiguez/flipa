import asyncio
import json
from numpy import place
import streamlit as st
from web3 import Web3
# from web3.middleware import geth_poa_middleware # only needed for PoA networks like BSC
import requests
from websockets import connect
from eth_abi import decode_single, decode_abi
import math

import pandas as pd
# adapter = requests.sessions.HTTPAdapter(pool_connections=50000, pool_maxsize=50000) # pool connections and max size are for HTTP calls only, since we are using WS they are not needed. 
session = requests.Session()
w3 = Web3(Web3.WebsocketProvider("wss://mainnet.infura.io/ws/v3/43b2d6f15d164cb4bbe4d4789831f242"))
# w3.middleware_onion.inject(geth_poa_middleware, layer=0) # only needed for PoA networks like BSC
# df = pd.DataFrame(columns=['from', 'to', 'value'])
false = False
async def get_event():
    # global df
    async with connect("wss://mainnet.infura.io/ws/v3/43b2d6f15d164cb4bbe4d4789831f242") as ws:
        await ws.send(json.dumps(
        {"id": 1, "method": "eth_subscribe", "params": 
        ["logs", 
        {"address": "0xdac17f958d2ee523a2206206994597c13d831ec7",
        "topics":["0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"]
        }
        ]
        }
        )
        )
        subscription_response = await ws.recv()

        print(subscription_response)
        while True:
            # try:
            message = await asyncio.wait_for(ws.recv(), timeout=60)

            # st.json(message)
            # df = df.append(pd.DataFrame(list(decode_abi('(address,address,address,address,uint256,uint256)',bytearray.fromhex(((json.loads(json.dumps(message)))["params"]["result"]["data"][2:])))),columns=['blockNumber','blockHash','transactionHash','transactionIndex','from','to','value','gas','gasPrice','input']),ignore_index=True)
            # with placeholder2:
            #     st.write(df)
            # st.dataframe(df)
            # print(list(decode_single('(address,address,address,address,uint256,uint256)',bytearray.fromhex(((json.loads(json.dumps(message)))["params"]["result"]["data"][2:])))))
            # print(decode_single('(address,address,address,address,uint256,uint256)',bytearray.fromhex(((json.loads(json.dumps(message)))["params"]["result"]["data"][2:]))))
            # data = message
            lord_jesus = json.loads(message)
            lord_jesus = json.dumps(lord_jesus)
            lord_jesus = json.loads(lord_jesus)
            lord_jesus = lord_jesus["params"]["result"]
            number = lord_jesus["data"][2:]
            addy1 = lord_jesus["topics"][1][2:]
            addy2 = lord_jesus["topics"][2][2:]
            number = decode_single('(uint256)',bytearray.fromhex(number))
            addy1 = decode_single('(address)',bytearray.fromhex(addy1))
            addy2 = decode_single('(address)',bytearray.fromhex(addy2))
            number = number[0]
            number = number / math.pow(10,6)
            addy1 = addy1[0]
            addy2 = addy2[0]
            # df = pd.DataFrame(columns=['from', 'to', 'value'])
            # df = df.append(pd.DataFrame(list([addy1,addy2,number]),columns=['from','to','value']),ignore_index=True)
            print(number)
            print(addy1)
            print(addy2)
            st.write(number)
            st.write(addy1)
            st.write(addy2)
            # print(df)
                # st.write(data)
                # st.write(df)
                # print(decode_single('(address,address,address,address,uint256,uint256)',bytearray.fromhex(((json.loads(json.dumps(message)))["params"]["result"]["data"][2:]))))

            #     pass
            # except:
            #     pass
# st.json(message)

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
while True:
    loop.run_until_complete(get_event())
# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)
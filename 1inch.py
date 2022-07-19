import ccxt
import streamlit as st
import pandas as pd
from itertools import accumulate
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from itertools import chain
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta
import math
import asyncio
import os
import sys
from pprint import pprint
import json
from datetime import datetime
import requests  

tokens_list = requests.get(f"https://api.1inch.io/v4.0/1/tokens")
tokens_list = json.loads(tokens_list.text)
tokens_list = tokens_list["tokens"]
tokens_list = pd.DataFrame(tokens_list)
tokens_list = tokens_list.T
tokens_list = tokens_list.reset_index()
tokens_list = tokens_list.drop(columns=['index','logoURI', 'tags', 'eip2612', 'isFoT', 'synth', 'displayedSymbol'])

(tokens_list).head()
ls = ['0xf01a670973edc81865ebb9f68b10c47c31afc133', '0xae7ab96520de3a18e5e111b5eaab095312d7fe84', '0x7d1afa7b718fb893db30a3abc0cfc608aacfebb0', '0xf01a670973edc81865ebb9f68b10c47c31afc133', 340000000000000000, 564397840925300413418]
ls2 = ['0xf01a670973edc81865ebb9f68b10c47cpenis31afc133', '0xae7ab96520de3a18e5e111b5eaab095312d7fe84', '0x7d1afa7b718fb893db30a3abc0cfc608aacfebb0', '0xf01a670973edc81865ebb9f68b10c47c31afc133', 340000000000000000, 564397840925300413418]


now = datetime.now()

ls = pd.DataFrame([ls], columns=['a', 'b', 'c', 'd', 'e', 'f'])
ls2 = pd.DataFrame([ls2], columns=['a', 'b', 'c', 'd', 'e', 'f'])
ls = ls.append(ls2, ignore_index=True)
ls['symbol1'] = [tokens_list.loc[tokens_list['address'] == b, 'symbol'].values[0] for b in ls['b']]
ls['symbol2'] = [tokens_list.loc[tokens_list['address'] == b, 'symbol'].values[0] for b in ls['c']]

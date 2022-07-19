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
  

st.subheader("""Cash n Carry Strat - spot vs dated """)

c1 = st.checkbox('Buy/Sell spread ? (buy=long spot/sell future // sell=short spot/buy future)', False)
if c1: 
    st.write("Yalla !!! Lets buy send a BUY LIMIT ORDER in the Trading Market ")
else: st.write("Yalla !!! Lets send a SELL LIMIT ORDER in the Trading Market ")

Trade_Size = st.number_input("please enter USD size to hedge in the hedging market")
Lending_rate = st.number_input("lending/borring rate") 

if c1: 
    spot_position_to_expiry = input("spot price to expiry")
    long_spot_position_to_expiry = (min_value_spot * (1 - ((latest_rateAPY_spot/1000)*(pct_expiry_dated/100))))
else : short_spot_position_to_expiry = (max_value_spot * (1 - ((latest_rateAPY_spot/1000)*(pct_expiry_dated/100))))


# 

# PREMIUM_LONG_SPOT_SHORT_DATED_FUTURE = (max_value_dated_futures - long_spot_position_to_expiry) 
# PREMIUM_SHORT_SPOT_LONG_DATED_FUTURE = (short_spot_position_to_expiry - min_value_dated_futures) 

# PREMIUM_LONG_SPOT_SHORT_DATED_FUTURE_APY = PREMIUM_LONG_SPOT_SHORT_DATED_FUTURE / (min_value_spot * (pct_expiry_dated/100)) * 100
# PREMIUM_SHORT_SPOT_LONG_DATED_FUTURE_APY = PREMIUM_SHORT_SPOT_LONG_DATED_FUTURE / (max_value_spot * (pct_expiry_dated/100)) * 100

# st.write("buy", min_value_spot, "spot", "sell", max_value_dated_futures, "dated_future")
# st.write("long_spot_position_to_expiry",long_spot_position_to_expiry)
# st.write("PREMIUM_LONG_SPOT_SHORT_DATED_FUTURE",PREMIUM_LONG_SPOT_SHORT_DATED_FUTURE)
# st.write(PREMIUM_LONG_SPOT_SHORT_DATED_FUTURE_APY, "% APY")
# st.write("sell", max_value_spot, "spot", "buy", min_value_dated_futures, "dated_future")
# st.write("short_spot_position_to_expiry",short_spot_position_to_expiry)
# st.write("PREMIUM_SHORT_SPOT_LONG_DATED_FUTURE",PREMIUM_SHORT_SPOT_LONG_DATED_FUTURE)
# st.write(PREMIUM_SHORT_SPOT_LONG_DATED_FUTURE, "% APY")
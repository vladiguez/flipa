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
  
st.set_page_config(layout="wide")
current_exchange = st.selectbox("exchange", ccxt.exchanges, index=21) 

if current_exchange== 'bitmex':
    exchange = ccxt.bitmex({
        'apiKey': 'NOAb2TuyuLgWkYbXOQGH-x9b',
        'secret': '_fAxf57mItdpX-A5KTxXRzJZY3zkeSKdCGlStwa95FAH81Gd',
    })
else:
    st.write("exchange not integrated")

if 'test' in exchange.urls:
    exchange.urls['api'] = exchange.urls['test']

market_data = pd.DataFrame(exchange.load_markets()).astype(str)
st.write(market_data)
Market_list = pd.DataFrame(market_data.columns).astype(str)


Trading_Market = st.selectbox("Trading Market", Market_list, index=406)
# st.write(index(Trading_Market))
Trading_Market_Precision = (market_data[Trading_Market]['precision'])
Trading_Market_Data = pd.DataFrame(exchange.fetch_ticker(Trading_Market)).astype(str)
Trading_Order_Book = exchange.fetchOrderBook(Trading_Market)
Trading_Order_Book_Bids = pd.DataFrame(Trading_Order_Book['bids'])
Trading_Order_Book_Asks = pd.DataFrame(Trading_Order_Book['asks'])

asks = Trading_Order_Book_Asks
bids = Trading_Order_Book_Bids

asks = asks.rename(columns={0: "price", 1: "size"})
bids = bids.rename(columns={0: "price", 1: "size"})
asks['accumulated_size']  = (list(accumulate(asks['size'])))
asks['accumulated_price']  = (asks['price']) * asks['size']
asks['accumulated_avg_price'] = (list(accumulate(asks['accumulated_price'])))  / asks['accumulated_size']
asks['cash_equivelant'] = asks['accumulated_size'] * asks['accumulated_avg_price']
bids['accumulated_size']  = (list(accumulate(bids['size'])))
bids['accumulated_price']  = (bids['price']) * bids['size']
bids['accumulated_avg_price'] = (list(accumulate(bids['accumulated_price'])))  / bids['accumulated_size']
bids['cash_equivelant'] = bids['accumulated_size'] * bids['accumulated_avg_price']
bidsdict = {
  tuple(bids['cash_equivelant']): tuple(bids['accumulated_avg_price'])
}

Trade_Size = st.number_input("please enter USD size to hedge in the hedging market", value = 1000)

#Display Trading Market Data

#TRADING MARKET ORDER BOOK
st.subheader("TRADING MARKET ORDER BOOK")

column = bids["price"]
best_bid = column.max()
st.write("best bid: ", best_bid)
column = asks["price"]
best_ask = column.min()
st.write("best ask: ", best_ask)
#res_key, res_val = min(bidsdict.items(), key=lambda x: abs(Trade_Size - x[1]))
#st.write((res_key))
best_ask_for_size = bidsdict[Trade_Size]
st.write("best_ask_for_size", best_ask_for_size)
bo_spread = best_ask - best_bid
st.write("bid/offer spread: ", bo_spread)
spread_in_bps = bo_spread/best_ask*1000
st.write("spread in bps: ", spread_in_bps, "bps")




# # TABLE BIDS AND OFFERS
# cols = st.columns(2)
# cols[0].subheader("bids")
# cols[0].write(bids)
# cols[1].subheader("asks")
# cols[1].write(asks)
    
# #ACCUMULATED ORDER BOOK
# fig = make_subplots(specs=[[{"secondary_y": True}]])
# # Add traces
# fig.add_trace(
#     go.Scatter(x=asks['price'], y=asks['accumulated_size'], name="asks"),
#     secondary_y=True,
# )
# fig.add_trace(
#     go.Scatter(x=bids['price'], y=bids['accumulated_size'], name="bids"),
#     secondary_y=True,
# )
# # Add figure title
# fig.update_layout(
#     title_text="accumulated orderbook"
# )
# # Set x-axis title
# st.plotly_chart(fig, use_container_width=True)

# #FLAT ORDER BOOK
# fig = make_subplots(specs=[[{"secondary_y": True}]])
# # Add traces
# fig.add_trace(
#     go.Bar(x=asks['price'], y=asks['size'], name="asks"),
#     secondary_y=True,
# )
# fig.add_trace(
#     go.Bar(x=bids['price'], y=bids['size'], name="bids"),
#     secondary_y=True,
# )
# # Add figure title
# fig.update_layout(
#     title_text="flat orderbook"
# )
# # Set x-axis title
# st.plotly_chart(fig, use_container_width=True)




Hedging_Market = st.selectbox("Hedge Market", Market_list)
Hedging_Market_Precision = (market_data[Hedging_Market]['precision'])
Hedging_Market_Data = pd.DataFrame(exchange.fetch_ticker(Hedging_Market)).astype(str)
Hedging_Order_Book = exchange.fetchOrderBook(Hedging_Market)
Hedging_Order_Book_Bids = pd.DataFrame(Hedging_Order_Book['bids'])
Hedging_Order_Book_Asks = pd.DataFrame(Hedging_Order_Book['asks'])


#Display Hedging Market Data

#HEDGING MARKET ORDER BOOK
st.subheader("HEDGING MARKET ORDER BOOK")

asks = Hedging_Order_Book_Asks
bids = Hedging_Order_Book_Bids

asks = asks.rename(columns={0: "price", 1: "size"})
bids = bids.rename(columns={0: "price", 1: "size"})
asks['accumulated_size']  = (list(accumulate(asks['size'])))
asks['accumulated_price']  = (asks['price']) * asks['size']
asks['accumulated_avg_price'] = (list(accumulate(asks['accumulated_price'])))  / asks['accumulated_size']
asks['cash_equivelant'] = asks['accumulated_size'] * asks['accumulated_avg_price']
bids['accumulated_size']  = (list(accumulate(bids['size'])))
bids['accumulated_price']  = (bids['price']) * bids['size']
bids['accumulated_avg_price'] = (list(accumulate(bids['accumulated_price'])))  / bids['accumulated_size']
bids['cash_equivelant'] = bids['accumulated_size'] * bids['accumulated_avg_price']


column = bids["price"]
best_bid = column.max()
st.write("best bid: ", best_bid)
column = asks["price"]
best_ask = column.min()
st.write("best ask: ", best_ask)
bo_spread = best_ask - best_bid
st.write("bid/offer spread: ", bo_spread)
spread_in_bps = bo_spread/best_ask*1000
st.write("spread in bps: ", spread_in_bps, "bps")






# # TABLE BIDS AND OFFERS
# cols = st.columns(2)
# cols[0].subheader("bids")
# cols[0].write(bids)
# cols[1].subheader("asks")
# cols[1].write(asks)
    

# #ACCUMULATED ORDER BOOK
# fig = make_subplots(specs=[[{"secondary_y": True}]])
# # Add traces
# fig.add_trace(
#     go.Scatter(x=asks['price'], y=asks['accumulated_size'], name="asks"),
#     secondary_y=True,
# )
# fig.add_trace(
#     go.Scatter(x=bids['price'], y=bids['accumulated_size'], name="bids"),
#     secondary_y=True,
# )
# # Add figure title
# fig.update_layout(
#     title_text="accumulated orderbook"
# )
# # Set x-axis title
# st.plotly_chart(fig, use_container_width=True)



# #FLAT ORDER BOOK
# fig = make_subplots(specs=[[{"secondary_y": True}]])
# # Add traces
# fig.add_trace(
#     go.Bar(x=asks['price'], y=asks['size'], name="asks"),
#     secondary_y=True,
# )
# fig.add_trace(
#     go.Bar(x=bids['price'], y=bids['size'], name="bids"),
#     secondary_y=True,
# )
# # Add figure title
# fig.update_layout(
#     title_text="flat orderbook"
# )
# # Set x-axis title
# st.plotly_chart(fig, use_container_width=True)



placeholder = st.empty()
while True:
    orders_hist = exchange.fetchOpenOrders()
    orders_hist = pd.DataFrame(orders_hist)
    with placeholder:
            if orders_hist.empty:
                st.write('no open orders')
            else:
                st.write(orders_hist)
                orders_hist = orders_hist[orders_hist.status != 'canceled']
                # orders_hist = orders_hist[orders_hist.status != 'closed']
                orders_hist_id_df = pd.DataFrame(orders_hist['id'])
                id = orders_hist_id_df
                order_cancel_df = pd.DataFrame()
                cancel_df = pd.DataFrame()
                cancelAllOrders = exchange.cancelAllOrders()
                st.write("canceled, yalla")

            order_init_bid = exchange.createLimitBuyOrder(symbol=Trading_Market,price=mm_bid_price,amount=mm_bid_size)
            order_df_bid = order_df_bid.append(order_init_bid, ignore_index=True)
         







   
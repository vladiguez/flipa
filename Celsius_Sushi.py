import plotly.express as px
import pandas as pd
import json
import requests
import streamlit as st

from sys import version, exit

from distutils import errors
from distutils.log import error
import streamlit as st
import pandas as pd 
import numpy as np
import altair as alt
from itertools import cycle
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode
import pandas as pd
import pandas_profiling
import streamlit as st

# from streamlit_gallery.utils.readme import readme
from streamlit_pandas_profiling import st_profile_report
st.set_page_config(layout="wide")

Celsius_sushi_crosschain_swaps = "https://node-api.flipsidecrypto.com/api/v2/queries/0ed37bbe-7a76-41e2-bad9-e6deadee0b91/data/latest"
Celsius_sushi_crosschain_borrowing = "https://node-api.flipsidecrypto.com/api/v2/queries/06dd8006-fdf6-4208-9565-892a26577842/data/latest"
Celsius_sushi_crosschain_lending = "https://node-api.flipsidecrypto.com/api/v2/queries/2c61dea1-4e7f-481e-aee7-f65b4fd25106/data/latest"
Celsius_sushi_ethereum_swaps = "https://node-api.flipsidecrypto.com/api/v2/queries/83f286db-0e26-4c6c-9bf3-ebf97b6bd548/data/latest"
Celsius_sushi_polygon_swaps = "https://node-api.flipsidecrypto.com/api/v2/queries/50f5c17c-b0f2-41df-bc4f-84a38044255b/data/latest"
Celsius_sushi_distrib_rewards = "https://node-api.flipsidecrypto.com/api/v2/queries/ad86b1bc-abc3-4f4e-a0b4-7f673a424dea/data/latest"
Celsius_sushi_ethereum_staking = "https://node-api.flipsidecrypto.com/api/v2/queries/459ede1c-ada4-4c66-a065-8c99de8b4bb9/data/latest"
Celsius_sushi_polygon_staking = "https://node-api.flipsidecrypto.com/api/v2/queries/2426b726-5fcd-4f90-aedc-21b9807cf4ed/data/latest"



st.subheader("Crosschain_swaps")
df_Celsius_sushi_crosschain_swaps = pd.read_json(
    Celsius_sushi_crosschain_swaps,
    convert_dates=["TIMESTAMP_NTZ"],
)
st.write(df_Celsius_sushi_crosschain_swaps)
#############################################

st.subheader("Crosschain_borrowing")
df_Celsius_sushi_crosschain_borrowing = pd.read_json(
    Celsius_sushi_crosschain_borrowing,
    convert_dates=["TIMESTAMP_NTZ"],
)
st.write(df_Celsius_sushi_crosschain_borrowing)
#############################################

st.subheader("Crosschain_lending")
df_Celsius_sushi_crosschain_lending = pd.read_json(
    Celsius_sushi_crosschain_lending,
    convert_dates=["TIMESTAMP_NTZ"],
)
st.write(df_Celsius_sushi_crosschain_lending)
#############################################

st.subheader("Ethereum_swaps")
df_Celsius_sushi_ethereum_swaps = pd.read_json(
    Celsius_sushi_ethereum_swaps,
    convert_dates=["TIMESTAMP_NTZ"],
)
st.write(df_Celsius_sushi_ethereum_swaps)
#############################################

st.subheader("Polygon_swaps")
df_Celsius_sushi_polygon_swaps = pd.read_json(
    Celsius_sushi_polygon_swaps,
    convert_dates=["TIMESTAMP_NTZ"],
)
st.write(df_Celsius_sushi_polygon_swaps)
#############################################

st.subheader("Distributed_rewards")
df_Celsius_sushi_distrib_rewards = pd.read_json(
    Celsius_sushi_distrib_rewards,
    convert_dates=["TIMESTAMP_NTZ"],
)
st.write(df_Celsius_sushi_distrib_rewards)
#############################################

st.subheader("Ethereum_staking")
df_Celsius_sushi_ethereum_staking = pd.read_json(
    Celsius_sushi_ethereum_staking,
    convert_dates=["TIMESTAMP_NTZ"],
)
st.write(df_Celsius_sushi_ethereum_staking)
#############################################

st.subheader("Polygon_staking")
df_Celsius_sushi_polygon_staking = pd.read_json(
    Celsius_sushi_polygon_staking,
    convert_dates=["TIMESTAMP_NTZ"],
)
st.write(df_Celsius_sushi_polygon_staking)
#############################################


merged_df = pd.merge(df_Celsius_sushi_ethereum_swaps, df_Celsius_sushi_ethereum_staking, on="HOUR")
st.write(merged_df)

# def gen_report(df):

#         pr = gen_profile_report(df, explorative=True)

#         st.write(df)

#         with st.expander("REPORT", expanded=True):
#             st_profile_report(pr)


# @st.cache(allow_output_mutation=True)
# def gen_profile_report(df, *report_args, **report_kwargs):
#     return df.profile_report(*report_args, **report_kwargs)
# gen_report_click = st.checkbox("Generate report", False)
# if gen_report_click:
#     gen_report(df=merged_df)
# df = merged_df

st.subheader("CELIUS on-chain activity on SUSHISWAP")
st.write("This reports will propose an analyze of CELIUS on chain activity on SUSHISWAP. It presents informations from different angles.")
st.write("We started by identifying all Celsius Project Names: celsius,celsiusx,celsius network. Then we extract Crosschain data, swap, lending and borrowing. And then Focus on Ethereum Mainnet and Polygon, Swaps, Staking, Rewards activity.")
st.write("We rapidly noticed that Celius was only active on ETHEREUM Mainnet, nothing on Polygon or any toher blockchain. Also Celsius had no lending and borrowing crosschain activity ")
st.write("We could not find any reward distributed on Sushi as well.")
st.write("Consequently, we will focus on the activity that we observed on Mainnet, In flow, outflow, and staking.")


st.subheader("CELSIUS CROSSCHAIN ACTIVITY")
st.write("IN FLOWS")
st.write("all the Assets - USD equivalent - token name and volumes. Those flows could come from swap, farming LDO, CVX, AAVE are well represented." )
st.plotly_chart(px.scatter(df_Celsius_sushi_crosschain_swaps, y ="AMOUNT_IN_USD", x ="SYMBOL_IN", color="BLOCKCHAIN"), use_container_width=True)
st.plotly_chart(px.scatter(df_Celsius_sushi_crosschain_swaps, y ="AMOUNT_IN_USD", x ="BLOCK_TIMESTAMP", color="SYMBOL_IN"), use_container_width=True)

st.write("OUT FLOWS")
st.write("all the Assets - USD equivalent - token name and volumes. Those flows could come from swap, farming LDO, CVX, AAVE are well represented." )
st.plotly_chart(px.scatter(df_Celsius_sushi_crosschain_swaps, y ="AMOUNT_OUT_USD", x ="SYMBOL_OUT", color="BLOCKCHAIN"), use_container_width=True)
st.plotly_chart(px.scatter(df_Celsius_sushi_crosschain_swaps, y ="AMOUNT_OUT_USD", x ="BLOCK_TIMESTAMP", color="SYMBOL_OUT"), use_container_width=True)
#######################################

st.subheader("CELSIUS SUSHI- MAINNET ACTIVITY ")
st.write("IN FLOWS")
st.plotly_chart(px.bar(df_Celsius_sushi_ethereum_swaps, y ="AMOUNT_IN_USD", x ="SYMBOL_IN", color="SYMBOL_IN"), use_container_width=True)
st.plotly_chart(px.scatter(df_Celsius_sushi_ethereum_swaps, y =["SYMBOL_IN", "AMOUNT_IN_USD"], x ="BLOCK_TIMESTAMP", color="AMOUNT_IN_USD"), use_container_width=True)
st.write("OUT FLOWS")
st.plotly_chart(px.bar(df_Celsius_sushi_ethereum_swaps, y ="AMOUNT_OUT_USD", x ="SYMBOL_OUT", color="SYMBOL_OUT"), use_container_width=True)
st.plotly_chart(px.scatter(df_Celsius_sushi_ethereum_swaps, y =["SYMBOL_OUT", "AMOUNT_OUT_USD"], x ="BLOCK_TIMESTAMP", color="AMOUNT_OUT_USD"), use_container_width=True)
#######################################

st.subheader("CELSIUS STAKING activity on SUSHI-ETHEREUM MAINNET")
st.plotly_chart(px.scatter(df_Celsius_sushi_ethereum_staking, y ="EVENT_NAME", x ="CONTRACT_NAME"), use_container_width=True)

#######################################

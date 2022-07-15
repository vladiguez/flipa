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

def gen_report(df):

        pr = gen_profile_report(df, explorative=True)

        st.write(df)

        with st.expander("REPORT", expanded=True):
            st_profile_report(pr)


@st.cache(allow_output_mutation=True)
def gen_profile_report(df, *report_args, **report_kwargs):
    return df.profile_report(*report_args, **report_kwargs)
gen_report_click = st.checkbox("Generate report", False)
if gen_report_click:
    gen_report(df=merged_df)
df = merged_df


st.subheader("GAS PRICE vs ASSET PRICES")
st.write("In the chart, ETH prices does not really influence gas price. We clearly see high fees on both range of the ETH price. It s less obvious for Polygon though. ")
st.plotly_chart(px.scatter(merged_df, x="MATICUSD_AVG", y="PRICE", color="EGAS_PRICE_AVG_USD"), use_container_width=True)

st.subheader("ETH GAS PRICE vs ETH PRICE")
st.write("More in details, on ETH we see high fees in both sides of the ETH price range")
st.plotly_chart(px.bar(df, y ="EGAS_PRICE_AVG_USD", x ="HOUR", color="PRICE"), use_container_width=True)

st.subheader("POLYGON GAS PRICE vs MATIC PRICE")
st.write("Again here, we can t really say the MATIC price influence the Gas Price")
st.plotly_chart(px.bar(df, y ="GAS_PRICE_AVG_USD", x ="HOUR", color="MATICUSD_AVG"), use_container_width=True)

st.subheader("MARKET IMPACT on ETH and MATIC GAS PRICES")
st.write("The chart is very interesting as we see High Gas prices in the higher and lower range of the asset price. But more than that, we notice a drop a Gas prices and when we observe big price change. Litteraly, we can start that market volatility as a bigger impact on GAS prices than the the ASSET prices aboslute value")
st.plotly_chart(px.scatter(df, y =["GAS_PRICE_AVG_USD", "EGAS_PRICE_AVG_USD"], x ="HOUR", color="PRICE", log_y=True), use_container_width=True)

st.subheader("MARKET IMPACT on ETH and MATIC TRANSACTION FEES")
st.write("The chart focus on fees paid per hour on ETH and Polygon. Unlike the gas price, we observe a spike in transaction fees during volatility market drop.")
st.plotly_chart(px.scatter(df, y =["PFEES", "EFEES_USD", "PRICE"], x ="HOUR", color="PRICE", log_y=True), use_container_width=True)

st.subheader("POLYGON FEES vs MATIC GAS PRICE")
st.write("More in details, this chart is very interesting as we observe the Negative Correlation between GAS price and PAID FEES")
st.plotly_chart(px.scatter(df, y =["PFEES", "GAS_PRICE_AVG_USD"], x ="HOUR", log_y=True), use_container_width=True)

st.subheader("ETH FEES vs ETH GAS PRICE")
st.write("Same on ETH, Negative Correlation between GAS price and PAID FEES ")
st.plotly_chart(px.scatter(df, y =["EFEES_USD", "EGAS_PRICE_AVG_USD"], x ="HOUR", log_y=True), use_container_width=True)

st.write("The Negative correlation is counter Intuitive, so in order to understand how the could happen, we will have a close look in Gas limit efficiency")

st.subheader("MATIC GAS LIMIT EFFICIENCY")
st.write("Very interesting chart showing how Market volatily impacts the GAS LIMIT efficiency")
st.plotly_chart(px.scatter(df, y ="PCT_AVG_GAS_LIMIT_EFFICIENCY_PER_TRANSACTION", x ="HOUR", color="MATICUSD_AVG", log_y=True), use_container_width=True)
    
st.subheader("MATICS GAS LIMIT EFFICIENCY")
st.write("SAME on ETH, the Market volatily impacts the GAS LIMIT efficiency")
st.plotly_chart(px.scatter(df, y ="PCT_AVG_EGAS_LIMIT_EFFICIENCY", x ="HOUR", color="PRICE", log_y=True), use_container_width=True)
    # pip install pandas_profiling --user
    # pip install streamlit_pandas_profiling --user

st.subheader("CONSEQUENTLY")
st.write("Even though we observe a drop in GAS PRICE due to ASSET PRICE drop, during a high volatility period, GAS LIMIT use becomes more Ineficiency reflecting the market panic, or the emergency of each transaction to be validated.")
st.write("Last observation regarding Polygon FEES, we observe a strong drop in transaction fees since the 5th of July, but we can't really dig deeper into that direction because of a lack of data in FS Tables.")  
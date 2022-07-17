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
# from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode
import pandas as pd
# import pandas_profiling
import streamlit as st

# from streamlit_gallery.utils.readme import readme
# from streamlit_pandas_profiling import st_profile_report
st.set_page_config(layout="wide")

Velo_Duration = "https://node-api.flipsidecrypto.com/api/v2/queries/459ede1c-ada4-4c66-a065-8c99de8b4bb9/data/latest"
Wallets = "https://node-api.flipsidecrypto.com/api/v2/queries/6f9a4b58-cdfd-4cd2-bdfe-aba10defe56d/data/latest"
voting_power = "https://node-api.flipsidecrypto.com/api/v2/queries/43ce7324-3e0f-43f8-a0fd-f27be078eda7/data/latest"
#############################################
st.subheader("Lockin Duration")
df_Velo_Duration = pd.read_json(
    Velo_Duration,
    convert_dates=["TIMESTAMP_NTZ"],
)
st.write(df_Velo_Duration)


st.subheader("Lockin Duration Analysis")
st.write("Among the 3 main locking periods: short term (from 1 day to 2 weeks), mid term (1 year) and long term (4 years), we observe more volume on the very long term, meaning that LPers have globally a longer term staking strategy ")
st.plotly_chart(px.scatter(df_Velo_Duration, y ="VALUE", x ="LOCKIN_DURATION", color="DEPOSIT_TYPE", log_y=True), use_container_width=True)


#############################################

st.subheader("Wallets")
df_wallets = pd.read_json(
    Wallets,
    convert_dates=["TIMESTAMP_NTZ"],
)
st.write(df_wallets)

st.subheader("Wallets Analysis")
st.write("5 wallet locked more than +2M USD, with 1 winner close to 6M USD locked on short term. Still we observe multiple wallets with decent volumes (in the 500k USD area) with a 4 year lockin duration")
st.plotly_chart(px.scatter(df_wallets, y ="TOTAL_VOLUME_LOCKED", x ="PROVIDER", color="AVG_LOCKIN_DURATION"), use_container_width=True)

#############################################
st.subheader("Wallets")
df_voting_power = pd.read_json(
    voting_power,
    convert_dates=["TIMESTAMP_NTZ"],
)
st.write(df_wallets)

st.subheader("Voting power Analysis")
st.write("We can see a large domination of the VELOUSDC pools which is preferred by the biggest Providers")
st.plotly_chart(px.bar(df_voting_power, y ="TOTAL_VOLUME_LOCKED", x ="POOL_NAME", color="PROVIDER"), use_container_width=True)
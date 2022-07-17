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

st.subheader("Lockin Duration")
df_Velo_Duration = pd.read_json(
    Velo_Duration,
    convert_dates=["TIMESTAMP_NTZ"],
)
st.write(df_Velo_Duration)
#############################################





# merged_df = pd.merge(df_Celsius_sushi_ethereum_swaps, df_Celsius_sushi_ethereum_staking, on="HOUR")
# st.write(merged_df)

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

st.subheader("Lockin Duration Analysis")
st.write("Among the 3 main locking periods: short term (from 1 day to 2 weeks), mid term (1 year) and long term (4 years), we observe more volume on the very long term, meaning that LPers have globally a longer term staking strategy ")
st.plotly_chart(px.scatter(df, y ="VALUE", x ="LOCKIN_DURATION", color="DEPOSIT_TYPE", log_y=True), use_container_width=True)

# st.write("OUT FLOWS")
# st.write("all the Assets - USD equivalent - token name and volumes. Those flows could come from swap, farming LDO, CVX, AAVE are well represented." )
# st.plotly_chart(px.scatter(df_Celsius_sushi_crosschain_swaps, y ="AMOUNT_OUT_USD", x ="SYMBOL_OUT", color="BLOCKCHAIN"), use_container_width=True)
# st.plotly_chart(px.scatter(df_Celsius_sushi_crosschain_swaps, y ="AMOUNT_OUT_USD", x ="BLOCK_TIMESTAMP", color="SYMBOL_OUT"), use_container_width=True)
# #######################################

# st.subheader("CELSIUS SUSHI- MAINNET ACTIVITY ")
# st.write("IN FLOWS")
# st.plotly_chart(px.bar(df_Celsius_sushi_ethereum_swaps, y ="AMOUNT_IN_USD", x ="SYMBOL_IN", color="SYMBOL_IN"), use_container_width=True)
# st.plotly_chart(px.scatter(df_Celsius_sushi_ethereum_swaps, y =["SYMBOL_IN", "AMOUNT_IN_USD"], x ="BLOCK_TIMESTAMP", color="AMOUNT_IN_USD"), use_container_width=True)
# st.write("OUT FLOWS")
# st.plotly_chart(px.bar(df_Celsius_sushi_ethereum_swaps, y ="AMOUNT_OUT_USD", x ="SYMBOL_OUT", color="SYMBOL_OUT"), use_container_width=True)
# st.plotly_chart(px.scatter(df_Celsius_sushi_ethereum_swaps, y =["SYMBOL_OUT", "AMOUNT_OUT_USD"], x ="BLOCK_TIMESTAMP", color="AMOUNT_OUT_USD"), use_container_width=True)
# #######################################

# st.subheader("CELSIUS STAKING activity on SUSHI-ETHEREUM MAINNET")
# st.plotly_chart(px.scatter(df_Celsius_sushi_ethereum_staking, y ="EVENT_NAME", x ="CONTRACT_NAME"), use_container_width=True)

#######################################

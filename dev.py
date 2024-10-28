#%%
from sec_yf.download_sec import download_and_prepare_data
from sec_yf.yahoo_finance import get_all_data

# Download and prepare data from SEC
download_and_prepare_data()

# Get all data from Yahoo Finance
get_all_data()
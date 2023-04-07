prc_dic = {
    '3000-01-15': 7.0400,
    '2020-01-14': 7.1100,
    '2020-01-13': 7.0200,
    '2020-01-02': 7.1600,
    '2020-01-03': 7.1900,
    '2020-01-06': 7.0000,
    '2020-01-07': 7.1000,
    '2020-01-08': 6.8600,
    '2020-01-09': 6.9500,
    '2020-01-10': 7.0000,
}

# replace '???' with the correct expression
sorted_keys = sorted([k for k in prc_dic.keys()])
prc_dic["2020-01-15"] = prc_dic.pop("3000-01-15")


tic = "QAN.AX"
start = f'{year}-01-01'
end = f'{year}-12-31'
pth = os.path.join(cfg.DATA, f'qan_prc_{year}, csv')
df = yf_example2.yf_prc_to_csv(tic=tic, pth=pth, start=start, end=end)

if __name__ == "__main__":
    year = 2020
    qan_prc_to_csv(year)


print ("The copyright symbol is: \u00A9")
print ("The copyright symbol has Unicode hex value: \\u00A9")

import pandas as pd

# Part (a)
# Create a pandas series called series_abc with
# index ['a', 'b', 'c'] and values [1, 2, 3]
series_abc = pd.Series(data = {'a':1, 'b':2, 'c':3})

# Part (b)
# Given the stock price-date dictionary prc_date
# listed below, create a pandas series series_stk
# with the dates as indices and the prices as values.
prc_date = {
    7.1600: '2020-01-02',
    7.1900: '2020-01-03',
    7.0000: '2020-01-06',
    7.1000: '2020-01-07',
    6.8600: '2020-01-08',
    6.9500: '2020-01-09',
    7.0000: '2020-01-10',
    7.0200: '2020-01-13',
    7.1100: '2020-01-14',
    7.0400: '2020-01-15',
    }


dates = pd.to_datetime(list(prc_date.values()))
prices = list(prc_date.keys())

series_stk = pd.Series(prices, index=dates)


# Part c
# Given the dictionary
dic = {i:i+1 for i in range(10000)}
# create a Pandas series called series_ones
# with indices from 0 through 9999 and with
# all values equal to 1.
# Do not use a secondary dictionary to create the series in Pandas.
# Instead, specify the data and index arguments directly.
series_ones = pd.Series(data=1, index=dic.keys())

""" main.py
Code challenge
"""

import numpy as np
import pandas as pd
# import yfinance as yf # Uncomment this line if you are wish to work with `yfinance` outside of Ed

# Write this function
def fx_code(from_cur, to_cur):
    """ Creates a string with the ticker required to download exchange rates
    using yfinance. The exchange rate will be the price of one unit of the `from_cur` in terms
    of the `to_cur`.

    Parameters
    ----------
    from_cur : str
        The ISO code of the currency to be priced.

    to_cur : str
        The ISO code of the currency with the value of one unit of `from_cur`.


    Returns
    -------
        A string that meets the `yfinance` ticker standards with ALL characters in upper case.
        The function should also be able to ignore leading and trailing spaces. For example,
        " aud", "Aud ", and " AUD " all are treated as "AUD" internally. See the
        Notes section below for more information.

    Notes
    -----
    Yahoo finance uses the following naming rules to define the ticker of the
    exchange rate AAA/BBB:
    usd/aud

    1. If AAA is the USD, then the ticker is "BBB=X", i.e., the second currency
       code with "=X" added at the end.
    2. If AAA is not the USD, then the ticker is "AAABBB=X"

    For example, the ticker for AUD/USD is "AUDUSD=X", while the ticker for
    USD/AUD is "AUD=X"

    So, if `from_cur=AAA` and the `to_cur=BBB`, the YF ticker will be:
    1. "BBB=X" if AAA is USD
    2. "AAABBB=X" if AAA is not the USD
    """

    cur_AAA = from_cur.strip().upper()
    cur_BBB = to_cur.strip().upper()

    if cur_AAA == "USD":
        return f"{cur_BBB}=X"
    else:
        return f"{cur_AAA}{cur_BBB}=X"

# get_fx is provided to demonstrate how you can download currency data from `yfinance`.
# Once your fx_code function above is correct, get_fx should work on a computer
# that has the `yfinance` package installed.
def get_fx(from_cur, to_cur, period=None, interval=None):
    """ Downloads the exchange rate between the `from_cur` and the `to_cur`.
    The exchange rate will be the price of one unit of the `from_cur` in terms
    of the `to_cur`

    Parameters
    ----------
    from_cur : str
        The ISO code of the currency to be priced

    to_cur : str
        The ISO code of the currency with the value of one unit of
        `from_cur`.

    period : str, None
        valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        (optional, default is '1mo')

    interval : str, None
        valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        (optional, default is '1d')

    Returns
    -------
    df
        Dataframe with daily exchange rates from Yahoo Finance

    """
    # Defaults
    if period is None:
        period = '1mo'
    if interval is None:
        interval = '1d'

    tic = fx_code(from_cur, to_cur)

    # fetches the data
    df = yf.download(tic, period=period, interval=interval)

    return df



import pandas as pd
import numpy as np
from unanswered import *

aud_usd_lst = [
    ('2020-09-08', 0.7280),
    ('2020-09-09', 0.7209),
    ('2020-09-11', 0.7263),
    ('2020-09-14', 0.7281),
    ('2020-09-15', 0.7285),
    ]

eur_aud_lst = [
    ('2020-09-08',  1.6232),
    ('2020-09-09',  1.6321),
    ('2020-09-10',  1.6221),
    ('2020-09-11',  1.6282),
    ('2020-09-15',  1.6288),
    ]

# Replace unanswered with your solution.
index = [key for key, value in aud_usd_lst]
data = [value for key, value in aud_usd_lst]
aud_usd_series = pd.Series(data=data, index=index)

index = [key for key, value in eur_aud_lst]
data = [value for key, value in eur_aud_lst]
eur_aud_series = pd.Series(data=data, index=index)
df = pd.DataFrame({'AUD/USD': aud_usd_series, 'EUR/AUD':eur_aud_series})

""" main.py

Code Challenge: Selecting observations in Pandas I

"""

import pandas as pd
import numpy as np

# IMPORTANT: please do not modify this import statement
from placeholders import put_your_answer_here


# The data frame `df` includes the following information
#
# |            | AUD/USD | EUR/AUD |
# |------------+---------+---------|
# | 2020-09-08 | 0.7280  | 1.6232  |
# | 2020-09-09 | 0.7209  | 1.6321  |
# | 2020-09-10 | NaN     | 1.6221  |
# | 2020-09-11 | 0.7263  | 1.6282  |
# | 2020-09-14 | 0.7281  | NaN     |
# | 2020-09-15 | 0.7285  | 1.6288  |
data = {
    'AUD/USD': [ 0.7280, 0.7209, np.nan, 0.7263, 0.7281, 0.7285,],
    'EUR/AUD': [ 1.6232, 1.6321, 1.6221, 1.6282, np.nan, 1.6288,],
    }
index = [ '2020-09-08', '2020-09-09', '2020-09-10', '2020-09-11', '2020-09-14', '2020-09-15',]
df = pd.DataFrame(data, index)



# Q1: What expression for `sel_q1` below will produce a DATA FRAME
# with the following information?
#
# |            | AUD/USD | EUR/AUD |
# +------------+---------+---------|
# | 2020-09-08 | 0.7280  | 1.6232  |
# | 2020-09-14 | 0.7281  |  NaN    |

# NOTE: replace `put_your_answer_here`
sel_q1 = ['2020-09-08', '2020-09-14']
q1 = df.loc[sel_q1]



# Q2: What expression for `start`, `stop` below will produce a DATA FRAME with
# following output?  (first two rows of `df`)
#
# |            | AUD/USD | EUR/AUD |
# +------------+---------+---------|
# | 2020-09-08 | 0.7280  | 1.6232  |
# | 2020-09-09 | 0.7209  | 1.6321  |

(start_q2, stop_q2) = (0,2)
q2 = df.iloc[start_q2:stop_q2]


# Q3: What expression for `start`, `stop` below will produce a DATA FRAME
# with following output?  (first two rows of `df`)
#
# |            | AUD/USD | EUR/AUD |
# +------------+---------+---------|
# | 2020-09-08 | 0.7280  | 1.6232  |
# | 2020-09-09 | 0.7209  | 1.6321  |

(start_q3, stop_q3) = ('2020-09-08', '2020-09-09')
q3 = df[start_q3:stop_q3]


# Q4: What expression for row_sel, col_sel below will produce a DATA FRAME
# with the following information?
#
# |            | AUD/USD |
# +------------+---------|
# | 2020-09-08 | 0.7280  |
# | 2020-09-09 | 0.7209  |

row_sel_q4 = ['2020-09-08', '2020-09-09']
col_sel_q4 = ['AUD/USD']
q4 = df.loc[row_sel_q4, col_sel_q4]




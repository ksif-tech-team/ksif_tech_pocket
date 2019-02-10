import pandas as pd
import pandas_datareader as pdr
from datetime import datetime as dt

# get all Code List listed
def get_code():

    # KOSPI
    kospi_code_df = \
        pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?marketType=stockMkt&method=download&searchType=13',
                     header=0)[0]
    kospi_code_df["market"] = "kospi"

    # KOSDAQ
    kosdaq_code_df = \
        pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?marketType=kosdaqMkt&method=download&searchType=13',
                     header=0)[0]
    kosdaq_code_df["market"] = "kosdaq"

    # KONNEX
    kkonex_code_df = \
        pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?marketType=konexMkt&method=download&searchType=13',
                     header=0)[0]
    kkonex_code_df["market"] = "kkonex"

    # Merge KSOPI, KOSDAQ, KONNEX
    code_df = pd.DataFrame()
    code_df = (kospi_code_df.append(kosdaq_code_df)).append(kkonex_code_df)

    # Remove unnecessary columns
    code_df = code_df[['종목코드', '회사명', 'market']]

    # Set column name
    code_df.종목코드 = code_df.종목코드.map('{:06d}'.format)

    # Change cloumn name to English
    code_df = code_df.rename(columns={'회사명': 'name', '종목코드': 'code'})

    return code_df


# Get price histroy of the firm
def get_a_price(code, source, start, end):
    # print(type(code))
    return pdr.DataReader(code + ".KS", source, start, end)

# Get all price histories listed
def get_prices(code_list, source, start, end):
    results = {}
    for code in code_list:
        # print(type(code), "=", code)
        results[code] = get_a_price('001040', source, start, end)

    return results




# main()
# Attributes of code_df(Dataframe) = {code, name, market}
code_df = pd.DataFrame(get_code())

code_list = list((get_code()).code)
print(len(code_list))
print(code_list[:10])
# code_list = ['001040','081150','013720']

source = 'yahoo'
start = '2019-01-15'
end = dt.now().strftime('%Y-%m-%d')

price_df = get_prices(code_list[:10], source, start, end)
print(price_df)
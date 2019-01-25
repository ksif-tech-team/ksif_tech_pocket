import pandas as pd
from record import *

CODE_FILE = "./code.csv"
# CODE_DF = pd.read_csv(CODE_FILE, index_col=[0])

# def code2name(code):
#     return CODE_DF[code]


def _pack_record(date, stocks, amount):
    if amount:
        return Record(date, [(stocks, "Temp Stock name", amount)])
    else:
        return Record(date, [(stock, "Temp stock name", amount) for stock, amount in stocks.items()])


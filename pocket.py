"""
Author  : Jiwoo Park
Date    : 2019. 1. 21
Desc    : Pocket - Balance Record System for Quant
"""
import sys
import pandas as pd

from record import Record
from datetime import datetime

PRICE_DF = pd.read_csv("./PRICE.csv", index_col=[0], parse_dates=[0])

class Pocket():
    """
    Balance System
    """
    def __init__(self, cash):
        """
        :param cash:    (Int) Amount of Cash in the pocket
        :param cur_stocks:  (Dataframe) of Stocks and its amount in the pocket
                            Which Column has [code, name, amount, purchase_date, purchase_price,
                                             purchase_volume, current_price, current_volume, return]
        """
        self.cash = cash
        columns = ["NAME", "AMOUNT", "DATE_PURCHASE", "PRICE_PURCHASE", "VOLUME_PURCHASE"]
        self.cur_stocks = pd.DataFrame(columns=columns) # cur_stock : code, name, amount, price_purchase, volume_purchase, return,
                                                        # price_current
        self.history = []
        self.logs = False

    def _pack_record(self, date, stocks, amount):
        if amount:
            return Record(date, [(stocks, "Temp Stock name", amount)])
        else:
            return Record(date, [(stock, "Temp stock name", amount) for stock, amount in stocks.items()])

    def order(self, date, stocks, amount=0):
        # Set cur_stocks and Add new record to history
        if not date:
            raise ValueError("Date is Required")

        self.set_cur_stocks(stocks, amount, date)
        new_record = self._pack_record(date, stocks, amount)
        self.history.append(new_record)

        if self.logs:
            print("Order Complete!")

        return True

    def set_one_stock(self, stock, amount, date):
        # buy or sell unit stock
        try:
            price_at_date = PRICE_DF.loc[date]
        except ValueError as e:
            print(e)
            print("Invalid Date to Order")

        try:
            price_of_firm = price_at_date[stock]
        except ValueError as e:
            print(e)
            print("Invalid Firm at Date")

        self.cur_stocks.loc[stock] = ["Stock Name", amount, date, price_of_firm, price_of_firm * amount]

    def set_cur_stocks(self, stocks, amount, date):
        if isinstance(stocks, type("")):
            # check difference between selling buying
            self.set_one_stock(stocks, amount, date)
        elif isinstance(stocks, type({})):
            # order multiple stocks with key and value from given dictionary
            for stock, amount in stocks.items():
                self.set_one_stock(stock, amount, date)

    def view_history(self):
        for hist in self.history:
            print(hist)


    def analyze(self, start, end):
        """
        :param start:   (datetime) Datetime starting analyzing date
        :param end:     (datetime) Datetime ending analyzing date
        :return:        (DataFrame) Dataframe that contain summary statistics
        """
        return


def get_update_list(new_portfolio_dict, portfolio_dict):
    enterance_dict = {}
    for stock_code, quantity in new_portfolio_dict.items():
        if stock_code not in portfolio_dict:
            enterance_dict[stock_code] = quantity

    exit_dict = {}
    for stock_code, quantity in portfolio_dict.items():
        if stock_code not in new_portfolio_dict:
            exit_dict[stock_code] = quantity

    update_stock_list = []

    update_portfolio_list = []


if __name__ == "__main__":
    pkt = Pocket(0)
    PRICE_DF = pd.read_csv("./PRICE.csv", index_col=[0], parse_dates=[0])

    pkt.order(datetime(2010, 9, 30), "A000030", 3)
    print(pkt.cur_stocks)

    sample_dict = {"A000660": 10, "A005930" : 30}
    pkt.order(datetime(2011, 9, 30), sample_dict)
    print(pkt.cur_stocks)
    pkt.view_history()

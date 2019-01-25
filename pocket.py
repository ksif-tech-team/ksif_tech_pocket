"""
Author  : Jiwoo Park
Date    : 2019. 1. 21
Desc    : Pocket - Balance Record System for Quant
"""
import sys
import pandas as pd

from record import Record
from datetime import datetime
import util

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


    def order(self, date, stocks, amount=0):
        # Set cur_stocks and Add new record to history
        success = True
        if not date:
            raise ValueError("Date is Required")

        try:
            new_record = util._pack_record(date, stocks, amount)
            self._set_cur_stocks(stocks, amount, date)
            self.history.append(new_record)
        except Exception as e:
            print("Your Order has been failed because of following reason.")
            success = False
            print(e)

        if self.logs and success:
            print(new_record)

        return success

    def _set_one_stock(self, stock, amount, date):
        # buy or sell unit stock
        try:
            price_at_date = PRICE_DF.loc[date]
        except Exception as e:
            print(e)
            raise ValueError("Invalid Date to Order")

        try:
            price_of_firm = price_at_date[stock]
            if not price_of_firm:
                raise ValueError("Ordered Stock doesn't have proper price info.")
        except Exception as e:
            print(e)
            raise ValueError("Ordered Stock is not available to trade.")

        # if stock already in position, how to do it??? --> Where to put cash concept in abstraction.
        self.cur_stocks.loc[stock] = ["Stock Name", amount, date, price_of_firm, price_of_firm * amount]

    def _set_cur_stocks(self, stocks, amount, date):
        if isinstance(stocks, type("")):
            # check difference between selling buying
            self._set_one_stock(stocks, amount, date)
        elif isinstance(stocks, type({})):
            # order multiple stocks with key and value from given dictionary
            for stock, amount in stocks.items():
                self._set_one_stock(stock, amount, date)

    def view_history(self):
        for hist in self.history:
            print(hist)

    def evaluate_cur_stocks(self):
        today = datetime.today()
        close_val = PRICE_DF.iloc[PRICE_DF.index.get_loc(today, method="ffill")]
        close_val = close_val[self.cur_stocks.index]
        close_val = pd.DataFrame({"PRICE_CURRENT" : close_val.values}, index=self.cur_stocks.index)
        evaluated_stocks = pd.merge(self.cur_stocks, close_val, left_index=True, right_index=True)
        evaluated_stocks = evaluated_stocks["AMOUNT"] * evaluated_stocks["PRICE_CURRENT"]
        evaluated_stocks = (self.cur_stocks["VOLUME_CURRENT"] / self.cur_stocks["VOLUME_PURCHASE"]) - 1
        return evaluated_stocks

    def analyze(self, start, end):
        """ Analyzing the performance of manager's pocket.
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
    pkt.logs = True # Activate Logging
    PRICE_DF = pd.read_csv("./PRICE.csv", index_col=[0], parse_dates=[0])

    pkt.order(datetime(2010, 9, 30), "A000030", 3)

    sample_dict = {"A000660": 10}
    pkt.order(datetime(2011, 9, 30), sample_dict)

    print(pkt.cur_stocks)

    sample_dict = {"A000660": 1}
    pkt.order(datetime(2012, 9, 28), sample_dict)
    print(pkt.evaluate_cur_stocks())
    print(pkt.cur_stocks)

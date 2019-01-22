"""
Author  : Jiwoo Park
Date    : 2019. 1. 21
Desc    : Pocket - Balance Record System for Quant
"""

from record import Record
from datetime import datetime

class Pocket():
    """
    Balance System
    """
    def __init__(self, cash, cur_stocks):
        """
        :param cash:    (Int) Amount of Cash in the pocket
        :param cur_stocks:  (Dataframe) of Stocks and its amount in the pocket
        """
        self.cash = cash
        self.cur_stocks = cur_stocks        # cur_stock : code, name, amount, price_purchase, price_evaluated, return,
                                                        # price_current
        self.history = []
        self.logs = False

    def order(self, stocks, amount=0, date=datetime.today()):
        # Set cur_stocks and Add new record to history
        self.set_cur_stocks(stocks, amount, date)
        new_record = Record(date, stocks)
        self.history.append(new_record)

        if self.logs:
            print("Order Complete!")
        return 1

    def set_one_stock(self, stock, amount, date):
        # buy or sell unit stock
        pass

    def set_cur_stocks(self, stocks, amount, date):
        if isinstance(stocks, type("")):
            # check difference between selling buying
            self.set_unit_stock(stocks, amount, date)
        elif isinstance(stocks, type({})):
            # order multiple stocks with key and value from given dictionary
            for stock, amount in stocks.items():
                self.set_unit_stock(stock,amount)



    def analyze(self, start, end):
        """
        :param start:   (datetime) Datetime starting analyzing date
        :param end:     (datetime) Datetime ending analyzing date
        :return:        (DataFrame) Dataframe that contain summary statistics
        """
        return



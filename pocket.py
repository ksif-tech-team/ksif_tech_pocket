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
        if isinstance(stocks, type("")):
            # order single stocks with amount
            # 1. modify cur_stocks
            # 2. add new record into history
            pass
        elif isinstance(stocks, type({})):
            # order multiple stocks with key and value from given dictionary
            pass

        if self.logs:
            print("Order Complete!")
        return 1

    def analyze(self, start, end):
        """
        :param start:   (datetime) Datetime starting analyzing date
        :param end:     (datetime) Datetime ending analyzing date
        :return:        (DataFrame) Dataframe that contain summary statistics
        """
        return



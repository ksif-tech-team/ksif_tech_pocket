"""
Author  : Jiwoo Park
Date    : 2019. 1. 21
Desc    : Record of transaction
"""
from datetime import datetime

class Record():

    def __init__(self, date, assets):
        """
        :param date:    Date that quant record
        :param assets:  Asset and it amount that quant wants to buy
        """
        self.date = date
        self.assets = assets


    def __str__(self):
        pass


    def evaluate(self):
        self.purchase_unit_price = None
        self.current_price = None

if __name__ == "__main__":
    rcd = Record(datetime(2019, 1, 3), "A000030",)


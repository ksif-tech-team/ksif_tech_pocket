"""
Author  : Jiwoo Park
Date    : 2019. 1. 21
Desc    : Pocket - Balance Record System for Quant
"""
import sys

class Pocket():
    """

    """
    def __init__(self, history):
        self.history = history


def get_update_list(new_portfolio_dict, portfolio_dict):



    # Enterance & clear(exit)
    enterance_dict = {}
    for stock_code, quantity in new_portfolio_dict.items():
        if stock_code not in portfolio_dict:
            enterance_dict[stock_code] = quantity

    # Clear(exit)
    exit_dict = {}
    for stock_code, quantity in portfolio_dict.items():
        if stock_code not in new_portfolio_dict:
            exit_dict[stock_code] = quantity

    # Modify(Ordering - buy/sell)


    update_stock_list = []






    update_portfolio_list = []
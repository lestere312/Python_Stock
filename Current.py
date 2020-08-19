import yfinance as yf
import pandas as pd
import glob
#import numpy
#import tensorflow as tf
import math
#from datetime import datetime

def mean(lst):
    return sum(lst) / len(lst)

def listToString(s):

    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += str(ele)
        str1 += "\n"
    # return string
    return str1

class players:
    def __init__(self):
        self.players = []

    def print(self):
        for i in range(0, len(self.players)):
            self.players[i].print()

    def make_move(self):
        for i in range(0, len(self.players)):
            self.players[i].make_move()

    def dividend(self, div):
        for i in range(0, len(self.players)):
            self.players[i].dividend(div)

    def split(self, spl):
        for i in range(0, len(self.players)):
            self.players[i].split(spl)

class player:
    def __init__(self, player, cash, strat):
        self.player = player
        self.strat = strat
        self.stock = 0
        self.cash = cash
        self.spent = 0

        self.stockArray = []
        self.arg_cost =0

        self.today = 0
        self.yesterday = 0
        self.change = 0

        self.div_prof = 0
    def make_move(self):
        self.next_day()

#
        if(self.stock == 0 and mean(history) <= self.today):
            self.buy()

        if len(self.stockArray) is not 0:
            self.arg_cost = mean(self.stockArray)
        else:
            self.arg_cost = 0

        if(self.today > self.arg_cost*(1+self.strat) and self.arg_cost != 0):
            self.sell()
        if(self.today < self.arg_cost*(1-self.strat) and self.change < 0 and self.arg_cost != 0):
            self.buy()

    def buy(self):
        if(self.today < self.cash):
            print("1 Bought")
            self.cash -= self.today
            self.stock += 1
            self.stockArray.append(self.today)

    def sell(self):
        print("1 Sold Player:"+ str(self.player))
        self.cash += self.today
        self.stock -= 1
        self.stockArray.pop()

    def next_day(self):
        self.change = float(change[len(history) - 1])
        self.yesterday = self.today
        self.today = float(history[len(history) - 1])
#        print("~~~Player" + str(self.player))

    def dividend(self, div):
        self.cash += div*self.stock
        self.div_prof += div*self.stock

    def split(self, split):
        stock_change = math.floor(self.stock*split) - self.stock
        print(stock_change)
        self.stock += stock_change
        for i in range(0, stock_change):
            self.cash += self.today
            self.buy()


    def print(self):
        print("~~~Player : " + str(self.player) + "~~~")
        print("Strat : " + str(self.strat))
        print("Mean : " + str(self.arg_cost))
        print("Buy : " + str(self.arg_cost*(1-self.strat)))
        print("Sell : " + str(self.arg_cost*(1+self.strat)))
        print("Cash : " + str(self.cash))
        print("Div-Profit : " + str(self.div_prof))
        print("Stock# : " + str(self.stock))
        print("Stocks : " + str(self.stock*float(history[len(history) - 1])))
        print("Total : " + str(self.cash + self.stock*float(history[len(history) - 1])))

stocks = pd.read_csv('amex_08_20.csv')

for i in range(0, len(stocks.index)):
    print(stocks.iat[i,1])
    print(stocks.iat[i,3])
    print(type(stocks.iat[i,2]) != type("ass"))
    print(isinstance(stocks.iat[i,3], str))
    print(isinstance(stocks.iat[i,5], str))
    stock = stocks.iat[i,0]



    if(type(stocks.iat[i,2]) != type("ass") and isinstance(stocks.iat[i,3], str) and isinstance(stocks.iat[i,5], str)):
        file1 = open(stock + "_data.txt","w")

        while True:
            try:
                actions = yf.Ticker(stock)
                break
            except:
                print("Stock did not work:(")

        while True:
            try:
                info = actions.info
                break
            except:
                print("Stock action did not work:(:(")


        out_string = ""
        out_array = []

        info_len = len(info)

        for i in range(0, info_len):
            out_array.append(info.popitem())
            out_string += str(out_array[len(out_array)-1])

            out_array.reverse()



        for t in range(0, info_len):
            file1.write(str(out_array[t]))
            file1.write("\n")

        print("Finished")

import yfinance as yf
import pandas as pd
#import tensorflow as tf
import math
from datetime import datetime

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

symbols = []

for i in range(0, len(stocks.index)):
    print(stocks.iat[i,1])
    print(stocks.iat[i,3])
    print(type(stocks.iat[i,2]) != type("ass"))
    print(isinstance(stocks.iat[i,3], str))
    print(isinstance(stocks.iat[i,5], str))
    stock = stocks.iat[i,0]



    if(type(stocks.iat[i,2]) != type("ass") and isinstance(stocks.iat[i,3], str) and isinstance(stocks.iat[i,5], str)):
        while True:
            try:
                data = yf.download(stock, start="1970-01-01", end="2020-08-30")
                break
            except:
                print("Stock did not work:(")

        while True:
            try:
                actions = yf.Ticker(stock)
                break
            except:
                print("Stock action did not work:(:(")


        out_string = ""
        out_array = []

        info_len = len(data.index)

        for i in range(0, info_len):
            out_array.append(data.iat[i, 3])

        out_array.reverse()

history = []
div = []
split = []
change = []
action_num = 0
#print(actions.actions.index[action_num])

players = players()


stat = 0
beg_cash = 100
for t in range(0, 10):
    if t is 0:
        stat = 0.05
        player0 = player(t, beg_cash, stat)
    else:
        stat = round(t*0.1, 1)
        player0 = player(t, beg_cash, stat)
    players.players.append(player0)


for i in range(len(data.index)):
    print("Day " + str(i) + ": " + str(data.index[i]))
    print(data.iat[i, 0])
    change.append((data.iat[i, 3] - data.iat[i, 0]))
    history.append(data.iat[i, 0])
#    print(actions.actions.index[action_num])
    if(actions.actions.index.size != action_num and actions.actions.empty == False):
        if(actions.actions.index[action_num] == data.index[i]):
            if(actions.actions.iat[action_num, 0] != 0):
#                print(type(actions.actions.index[action_num].asm8))
                players.dividend(actions.actions.iat[action_num, 0])
                print("There is a dividend")
                print("The dividend is : " + str(actions.actions.iat[action_num, 0]))
                div.append(actions.actions.iat[action_num, 0])
            if(actions.actions.iat[action_num, 1] != 0):
                players.split(actions.actions.iat[action_num, 1])
                print("There is a split")
                print("The split is : " + str(actions.actions.iat[action_num, 1]))
                split.append(actions.actions.iat[action_num, 1])
            print("ACTION HAPPENS HERERERER\n" + str(action_num) + "\n")
            action_num = action_num + 1
    players.make_move()



        print(type(data))
    print(out_array)

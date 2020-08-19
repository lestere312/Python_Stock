import yfinance as yf
import pandas as pd
#import tensorflow as tf
import math
from datetime import datetime
from matplotlib import pyplot as plt

def createList(r1, r2, t, k):
    list = []
    for i in range(r1, r2+1):
        list.append(round(i*t, k))
    return list

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

    def best(self):
        play = player(0, 0, 0)
        temp = 0
        best = 0
        for i in range(0, len(self.players)):
            play = self.players[i]
            temp = play.cash + play.stock*float(history[len(history) - 1])
            if(temp > best):
                best = temp
                answer = play
        return answer

    def worst(self):
        play = player(0, 0, 0)
        temp = 0
        best = 10000000000
        for i in range(0, len(self.players)):
            play = self.players[i]
            temp = play.cash + play.stock*float(history[len(history) - 1])
            if(temp < best):
                best = temp
                answer = play
        return answer

    def total(self):
        list = []
        for i in range(0, len(self.players)):
            play = self.players[i]
            list.append(play.cash + play.stock*float(history[len(history) - 1]))
        return list

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
        self.week_change = 0
        self.year_change = 0

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
#            print("1 Bought:"+ str(self.player))
            self.cash -= self.today
            self.stock += 1
            self.stockArray.append(self.today)

    def sell(self):
#        print("1 Sold Player:"+ str(self.player))
        self.cash += self.today
        self.stock -= 1
        self.stockArray.pop()

    def next_day(self):
        self.yesterday = self.today
        self.today = float(history[len(history) - 1])
        if(len(history) > 2):
                self.change = self.today - float(history[len(history) - 2])
        if(len(history) > 6):
            self.week_change = self.today - float(history[len(history) - 7])
        if(len(history) > 51):
            self.year_change = self.today - float(history[len(history) - 52])
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

stock = input("Please enter a stock ticker: ")

data = yf.download(stock, start="1970-01-01", end="2020-08-30")

actions = yf.Ticker(stock)

#writer = pd.ExcelWriter(stock + ".xlsx")


print(data)
#data.to_excel(writer,'Sheet1')
print(actions.actions)
#actions.actions.to_excel(writer,'Sheet2')
print(actions.actions.empty)
#print(actions.actions.index[0])
#print(actions.actions.iat[0, 0])
#print(actions.actions.iat[0, 1])
#print(data.size)
#print(data['High'])
#print(data['High'].size)
#print(len(data.index))
#print(data.columns[0])
print(actions.actions.index.size)



#writer.save()

file1 = open(stock + ".txt","w")

history = []
div = []
split = []
change = []
change_week = []
change_year = []
action_num = 0
#print(actions.actions.index[action_num])

players = players()


stat = 0
beg_cash = 1000
for t in range(0, 2000):
#    if t is 0:
#        stat = 0.05
#        player0 = player(t, beg_cash, stat)
#    else:
    stat = round(t*0.0005, 4)
    player0 = player(t, beg_cash, stat)
    players.players.append(player0)


for i in range(len(data.index)):
    print("Day " + str(i) + ": " + str(data.index[i]))
    print(data.iat[i, 3])
    change.append(players.players[0].change)
    change_week.append(players.players[0].week_change)
    change_year.append(players.players[0].year_change)
    history.append(data.iat[i, 3])
#    print(actions.actions.index[action_num])
#    if(actions.actions.index.size != action_num and actions.actions.empty == False):
#        if(actions.actions.index[action_num] == data.index[i]):
#            if(actions.actions.iat[action_num, 0] != 0):
#                print(type(actions.actions.index[action_num].asm8))
#                players.dividend(actions.actions.iat[action_num, 0])
#                print("There is a dividend")
#                print("The dividend is : " + str(actions.actions.iat[action_num, 0]))
#                div.append(actions.actions.iat[action_num, 0])
#            if(actions.actions.iat[action_num, 1] != 0):
#                players.split(actions.actions.iat[action_num, 1])
#                print("There is a split")
#                print("The split is : " + str(actions.actions.iat[action_num, 1]))
#                split.append(actions.actions.iat[action_num, 1])
#            print("ACTION HAPPENS HERERERER\n" + str(action_num) + "\n")
#            action_num = action_num + 1
    players.make_move()


print("\nHistory : ")
print(history)
print("~average: " + str(mean(history)))
print("~min : " + str(min(history)))
print("~max : " + str(max(history)))

print("\nChange : ")
print(change)
print("~average: " + str(mean(change)))
print("~min : " + str(min(change)))
print("~max : " + str(max(change)))

if div:
    print("\ndiv : ")
    print(div)
    print("~average: " + str(mean(div)))
    print("~min : " + str(min(div)))
    print("~max : " + str(max(div)))
else:
    print("\nNo Dividends")
if split:
    print("\nsplit : ")
    print(split)
    print("~average: " + str(mean(split)))
    print("~min : " + str(min(split)))
    print("~max : " + str(max(split)))
else:
    print("\nNo Splits")

    file1.write(listToString(history))

print(actions.info)

print("Best Player:")
print(players.best().print())

print("Worst Player:")
print(players.worst().print())

plt.plot(data.index, change, label='Day-Change')

plt.xlabel('Day', fontsize=18)

plt.ylabel('Day-Change', fontsize=16)

plt.show()

plt.plot(data.index, change_week, label='Week-Change')

plt.xlabel('Day', fontsize=18)

plt.ylabel('Week-Change', fontsize=16)

plt.show()

plt.plot(data.index, change_year, label='Year-Change')

plt.xlabel('Day', fontsize=18)

plt.ylabel('Year-Change', fontsize=16)

plt.show()

#print(players.print())
plt.plot(data.index, history, label='Price')

plt.xlabel('Day', fontsize=18)

plt.ylabel('Open-Price', fontsize=16)

plt.show()

scores = players.total()

x = createList(0, len(scores)-1, 0.0005, 4)

plt.plot(x, scores, label='Cash')

plt.xlabel('Sell/Buy-Ratio', fontsize=18)

plt.ylabel('Ending-Cash-1000Start', fontsize=16)

plt.show()

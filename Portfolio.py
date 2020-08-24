import yfinance as yf
import pandas as pd
import glob
import math
from matplotlib import pyplot as plt

class portfolio:
    def __init__(self):
        self.stocks = []
        self.sectors = []
        self.recemend = []

    def value(self):
        for i in range(0, len(self.stocks)):
            self.stocks[i].value = round(self.stocks[i].price * self.stocks[i].num, 4)

    def print(self):
        for i in range(0, len(self.stocks)):
            print(self.stocks[i].sym + ": " + str(self.stocks[i].value))
            print(str(self.stocks[i].num) + ": " + str(self.stocks[i].price))
            print(self.stocks[i].sector + ": " + self.stocks[i].indust)
        for t in range(0, len(self.sectors)):
            print(self.sectors[t].name + ": " + str(self.sectors[t].value))
            print(self.sectors[t].stocks)
            for r in range(0, len(self.recemend)):
                for y in range(0, len(self.recemend[r].name)):
                    print(self.recemend[r].name[y] + ": " + str(self.recemend[r].num))

    def plot(self):
        x = []
        y = []
        total = 0
        y_percent = []
        for t in range(0, len(self.sectors)):
            x.append(self.sectors[t].name)
            y.append(round(self.sectors[t].value, 4))
            total += round(self.sectors[t].value, 4)
#        for t in range(0, len(self.sectors)):
#            y_percent.append(round(y[t]/total,4))
#        fig = plt.figure()
#        ax = fig.add_axes([0,0,1,1])
        plt.bar(x, y)
        plt.xticks(x, x, rotation=90)
        plt.subplots_adjust(bottom=0.4, top=0.99)
        plt.title('Sectors')
        plt.show()


        cols = ['#A06CD5','#6247AA','#11B5E4', '#ECA400']

        plt.pie(y,
            labels=x,
            colors=cols,
            startangle=90,
            shadow= True,
            autopct='%1.1f%%')

        plt.title('Sectors')
        plt.show()


        a = []
        s = []
        u = []
        total = 0

        for t in range(0, len(self.recemend)):
            print("Rec: " + str(self.recemend[t].name))
            for v in range(0, len(self.recemend[t].name)):
                print("Rec: " + str(v) + self.recemend[t].name[v])
                if self.recemend[t].name[v] not in a:
                    a.append(self.recemend[t].name[v])
                    print("Rec val: " + str(self.recemend[t].value))
                    s.append(round(self.recemend[t].value, 4))
                    u.append(self.recemend[t].num)
                else:
                    index = a.index(self.recemend[t].name[v])
                    s[index] += round(self.recemend[t].value, 4)
                    u[index] += 1

        print(str(a))
        print(str(s))
        print(str(u))

        for l in range(0, len(s)):
            s[l] = round(s[l]/u[l], 4)


        print(str(a))
        print(str(s))
        print(str(u))

        plt.bar(a, u)
        plt.xticks(a, a, rotation=90)
        plt.subplots_adjust(bottom=0.4, top=0.99)
        plt.title('Rating by Number')
        plt.show()

        plt.pie(u,
            labels=a,
            colors=cols,
            startangle=90,
            shadow= True,
            autopct='%1.1f%%')
        plt.title('Rating by Number')
        plt.show()


        plt.bar(a, s)
        plt.xticks(a, a, rotation=90)
        plt.subplots_adjust(bottom=0.4, top=0.99)
        plt.title('Rating by Weight')
        plt.show()

        plt.pie(s,
            labels=a,
            colors=cols,
            startangle=90,
            shadow= True,
            autopct='%1.1f%%')
        plt.title('Rating by Weight')
        plt.show()

    def add_stock(self, stock):
        temp = 0
        print("Length: " + str(len(self.recemend)))


        temp2 = 0
        for k in range(0 , len(stock.eval)):
            for t in range(0 , len(self.recemend)):
                print("len(self.recemend[t].name)" + str(len(self.recemend[t].name)))
                for y in range(0, len(self.recemend[t].name)):
                    if self.recemend[t].name[y] in stock.eval[k]:
                        print(self.recemend[t].name)
                        print("add to eval " + stock.eval[k])
                        print(stock.eval[k])
                        self.recemend[t].num += 1
                        self.recemend[t].value = round(stock.price * stock.num, 4)
                        temp2 = 1
            if(temp2 == 0):
                for y in range(0, len(stock.eval)):
                    print("New Eval " + str(stock.eval[y]))
                    new_sec = eval()
                    new_sec.num = 1
                    new_sec.value = round((stock.price * stock.num), 4)
                    print("Val:" + str(new_sec.value))
                    new_sec.name.append(stock.eval[y])
                    self.recemend.append(new_sec)


        for t in range(0 , len(self.sectors)):
            if(self.sectors[t].name == stock.sector):
                print(t)
                print("add to sector " + stock.sector)
                print(str(stock.price))
                self.sectors[t].value = round(self.sectors[t].value + (stock.price * stock.num), 4)
                self.sectors[t].stocks.append(stock.sym)
                temp = 1
        if(temp == 0):
            print("New Sector " + stock.sector)
            new_sec = sector()
            new_sec.value = round(stock.price * stock.num, 4)
            new_sec.name = stock.sector
            new_sec.stocks.append(stock.sym)
            self.sectors.append(new_sec)
        self.stocks.append(stock)

class sector:
    def __init__(self):
        self.value = 0
        self.name = ""
        self.stocks = []

class stock_pos:
    def __init__(self):
        self.sym = ""
        self.num = 0
        self.price = 0
        self.sector = ""
        self.indust = ""
        self.value = 0
        self.eval = []

class eval:
    def __init__(self):
        self.name = []
        self.num = 0
        self.value = 0

port_file = "portaugust.csv"

#input("Enter file with stocks col 1 and quntity in col 3: ")

stocks = pd.read_csv(port_file)

port = portfolio()

temp = 0

for i in range(0, len(stocks.index)):
    stock = stock_pos()
    print("Line: " + str(i))
    try:
#        print(stocks.iat[i,0])
#        print(stocks.iat[i,0])
#        print(type(stocks.iat[i,0]))
#        print(stocks.iat[i,2])
        stock.num = int(stocks.iat[i,2])
        stock.sym = stocks.iat[i,0]
    except:
        print("Line did not work:(")

    if(stock.num > 0):
        while True:
            try:
                data = yf.Ticker(stock.sym)
                break
            except:
                print("Retry geting stock info")

        while True:
            try:
                info = data.info
                break
            except:
                print("Retrying geting data info")

        while True:
            try:
                recemend = data.recommendations
                break
            except:
                print("Retrying geting recemendations info")

        if recemend is not None:
            print(len(recemend.index))
            for i in range(0, len(recemend.index)):
#                print(type(recemend.index[i].year))
                if(recemend.index[i].year == 2020):
                    print(recemend.iat[i,1])
                    print(recemend.index[i].year)
                    stock.eval.append(recemend.iat[i,1])

        try:
            stock.indust = info["industry"]
        except:
            stock.indust = info["category"]

        try:
            stock.sector = info["sector"]
        except:
            stock.sector = info["category"]

        price = data.history(period="1d")
#        print(price)
        try:
            stock.price = price.iat[0,3]
        except:
            stock.price = 0
#        print(info)
        print("need:" + str(stock.eval))
        port.add_stock(stock)
#    print(type(stocks.iat[i,2]))
print(info)
port.value()
port.print()
port.plot()

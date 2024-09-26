import ExchangeClass
exch = ExchangeClass

price = int(input("The transfer amount is?\n"))
to = (input("to ?\n do you want halp [1]"))
if to == "1" :
    exch.shoe()
    to = input("to ?\n do you want halp [1]")

BOS = input("do you want bay or sale [1 or 2]")
to =to.upper()
if BOS == "2":
    totel = price*exch.exchange_rates_sale[to]
    print("is=" + str(totel))
elif BOS == "1":
    totel = price*exch.exchange_rates_purchase[to]
    print("is=" + str(totel))
else :
    print("wrong commant")
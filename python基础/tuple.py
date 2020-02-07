from collections import namedtuple

Stock = namedtuple("Stock", "symbol current high low")

Stock = Stock("Good", 613.30, high=635.56, low=510.35)

print(Stock.symbol)
print(Stock.high)


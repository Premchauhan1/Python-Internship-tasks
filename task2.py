import datetime
from forex_python.converter import CurrencyRates

c = CurrencyRates()
current_time = datetime.datetime.now()

src_currency = input("enter the source currency which you want to convert: ")
des_currency = input("enter the target currency to which you want to convert: ")
amount = int(input("enter the amount you want to convert: "))

current_rate=c.get_rate(src_currency,des_currency, current_time)
print("the current rate for converting", src_currency, "to", des_currency, "is: ", current_rate)

converted_amount = amount*current_rate
print("The converted amount is: ", round(converted_amount, 2))

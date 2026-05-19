import config

from quantvn.vn.data import get_stock_hist

df = get_stock_hist("VIC", resolution="1H")
print(df.tail())
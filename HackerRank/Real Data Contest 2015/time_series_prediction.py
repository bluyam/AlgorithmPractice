import sys
import numpy as np
import pandas as pd

def date_to_string(x):
    return pd.to_datetime(x).strftime('%m.%d')

def same_date(x, y):
    return date_to_string(x) == date_to_string(y)

def update_predictions(n, c, yc):
    if yc == 1:
        predicted_values.insert(c, n)
    else:
        predicted_values[c] = (predicted_values[c]*(yc-1)+n)/yc

date = np.datetime64("2012-10-01")

data = sys.stdin
predicted_values = []

day_count = int(data.readline().split("\n")[0])
final_date = date + np.timedelta64(day_count, 'D')
eof_date = final_date + np.timedelta64(30, 'D')

should_add = False
count = 0
year_count = 0

for line in data.readlines()[1:]:
    n = int(line.split("\n")[0])
    if should_add:
        update_predictions(n, count, year_count)
        count = count + 1
    if date_to_string(date) == date_to_string(final_date):
        should_add = True
        year_count = year_count + 1
    if same_date(date, eof_date):
        should_add = False
        count = 0
    date = date + np.timedelta64(1, 'D')

for val in predicted_values:
    print(val)

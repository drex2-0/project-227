import json
import csv
import steer
import throttle

data_from_csv=[""]

with open('data_set.txt', 'r') as f:
data_from_txt = json.loads(f.read())


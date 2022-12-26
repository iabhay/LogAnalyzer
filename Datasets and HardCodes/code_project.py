import csv
import numpy as np
import pandas as pd
import openpyxl
import datetime

filedata = pd.read_excel(
    "REMOTE PATH", "Sheet1")

dates = filedata['Date'].values.tolist()
times = filedata['Time'].values.tolist()
ips = filedata['IP'].values.tolist()
actions = filedata['action'].values.tolist()
count = 1
wlist = ["115.55.55.55", "90.0.0.0.0", "210.10.1.0", ""]

n = len(ips)
for i in range(n):
    if ips[i] != ips[i-1]:
        count = 1
    if ips[i] == ips[i-1] and count == 1:
        startDate = dates[i-1]
        startTime = times[i-1]
    if ips[i] == ips[i-1]:
        count += 1
    if count >= 5:
        if ips[i] not in wlist:
            endDate = dates[i]
            endTime = times[i]
            if startDate == endDate and startTime-endTime < 2:
                count = 1
                if actions[i] == "Client Error" | actions[i] == "Server Error":
                    print("blocked")

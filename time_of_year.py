import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

NDAYS = 365
MSperS = 1000
SperM = 60

song_dict = {}
font = {'weight' : 'bold',
        'size'   : 8}

plt.rc('font', **font)
artist = 'artistName'
track = 'trackName'
listen = 'msPlayed'
ts = 'endTime'
#band_thresh = 100
time_thresh = 30000
topN = 50

with open("anthony/MyData/stream_hist.json", "r") as read_file:
    data = json.load(read_file)

a = pd.DataFrame(data)

a.endTime = pd.to_datetime(a.endTime)
fig, ax = plt.subplots(layout='constrained')
a = a[~a[ts].dt.day.isin([4,5])]
ax = (a.groupby(a[ts].dt.hour)["msPlayed"].sum()).plot(kind="bar")#*(1.0/SperM)*(1.0/MSperS)*(1.0/NDAYS)).plot(kind="bar")
ax.grid(axis='y',linestyle='--',zorder=0)#ax.invert_yaxis()
#plt.yscale("log")
ax.set_xlabel("hour of the day")
ax.set_ylabel("Av min/day")

plt.show()

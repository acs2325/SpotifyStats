import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
from matplotlib import rcParams

#some style
rcParams.update({'figure.autolayout': True})

font = {'weight' : 'bold',
        'size'   : 8}

plt.rc('font', **font)

#names of dataframe columns
artist = 'artistName'
track = 'trackName'
time = 'msPlayed'

time_thresh = 10 #seconds
ms_s = 1000 #ms per second

def getDf(fpath = "andrew/MyData/stream_hist.json"):

    with open(fpath, "r") as read_file:

        data = json.load(read_file)

        return pd.DataFrame(data)
    
def sortByOccurences(a,columnn, N = -1):

    #get the number of occurences
    a['Occur'] = a.groupby(artist)[artist].transform('size')
    a = a.sort_values(by='Occur',  ascending=False)

    if N > -1:
        a = a[a[artist].isin(a[artist].unique()[:N])]
    
    return a

def timeCut(a,time_thresh = 30):

    #cut songs listened to for less than time_thresh seconds
    a = a[a[time] > time_thresh*ms_s]

    return a


def getTopNbyListens(a,N = 50, songs_stacked = True):

    a = sortByOccurences(timeCut(a),artist)

    max_len = a[track].nunique() #this is a big overestimate...
    bars = np.zeros((N,max_len))
    cats = []
    for j,art in enumerate(a[artist].unique()) : 
        if j == N: break
        cats.append(art)
        song_counts = a.query("{} == r'{}'".format(artist,art))[track].value_counts()
        bars[j,:len(song_counts)] = song_counts

    cats = cats[::-1]
    bars = bars[::-1]

    if not(songs_stacked):
        bars[:,0] = bars.sum(axis = 1)
        bars[:,1] = np.zeros(N)

    return ((cats,bars))

def plot_stacked_bar(tuptup,log = 0):

    '''
    takes a tuple : list of strings len N, numpy array x by N 
      ([cat1,cat2,...], [cat1 bar, cat2 bar,...])
    '''

    #max_len = a[track].nunique()
    #unpack input
    cats,bars = tuptup
    #get top counts (for axes range)
    top_cts = max(bars.sum(axis = -1))

    fig, ax = plt.subplots(layout='constrained')

    #intialize vector where prev histogram is stored (for stacking)
    lef=np.zeros(len(cats))

    for i in range(len(bars[:,0])):

        #plot one hist
        ax.barh(np.arange(len(cats)),bars[:,i],left=lef)
        #add to stack
        lef += bars[:,i]
        #lazy break condition
        if (bars[:,i].sum() == 0): break

    ax.set_yticks(np.arange(len(cats)), labels=cats)
    ax.grid(axis='x',linestyle='--',zorder=0)
    
    if log: plt.xscale("log"); ax.set_xlim(1,round(top_cts*10,100))
    else: ax.set_xlim(0,round(top_cts + .3*top_cts,100))

    plt.show()

def plot_compare_users(tuptupA,tuptupB):

    '''
    takes a tuple : list of strings len N, numpy array x by N 
      ([cat1,cat2,...], [cat1 bar, cat2 bar,...])
    '''

    #max_len = a[track].nunique()
    #unpack input
    cats,your_bars = tuptupA
    _,my_bars = tuptupB
    #get top counts (for axes range)
    top_cts = max(my_bars)

    df = pd.DataFrame({'Me': my_bars,'You': your_bars}, index=cats)

    #fig, ax = plt.subplots(layout='constrained')

    #ax.barh(np.arange(len(my_cats)),my_bars)
    #ax.barh(np.arange(len(cats)),your_bars)
    ax = df.plot.barh(color=['red','blue'])

    #ax.set_yticks(np.arange(len(your_cats)), labels=your_cats)
    ax.grid(axis='x',linestyle='--',zorder=0)
    
    #plt.xscale("log"); ax.set_xlim(1,round(top_cts*10,100))
    ax.set_xlim(0,round(top_cts + .3*top_cts,100))

    plt.show()

if __name__ == "__main__":

    andrews = getDf("andrew/MyData/stream_hist.json")
    tonys = getDf("anthony/MyData/stream_hist.json")

    plot_stacked_bar(getTopNbyListens(andrews, 75),1)
    plot_stacked_bar(getTopNbyListens(tonys, 75),1)

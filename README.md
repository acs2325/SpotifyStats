# SpotifyStats

Setup: If you request your data from spotify, it gets sent in the form of a folder called `MyData`. This repo is structured as follows: create a directory with your name, and place `MyData` inside. An example is given in the form of the `andrew` directory included. Scrpits are structured to read streaming history json files according to this structure. 

## quick stats

You can quickly print to screen your top `N` artists and number of listens for each by running `artist_by_listens.sh`, and similarly for tracks. Default user set to andrew, Default `N = 10`, but can be changed:
```
./tracks_by_listens.sh anthony 25
```
The command also pipes all artists or songs by N listens into a text file for posterity.

## plotting scripts

A plot of top listens by artist is obtained with `plots.py`. Current setup: read streaming history into a `.json` with a call to `getDf`, then plot a stacked bar hist obtained from `getTopNbyListens(user,N)`.

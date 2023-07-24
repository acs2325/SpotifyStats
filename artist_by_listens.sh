cat MyData/StreamingHist*.json | grep "artist" | sort | uniq -c | awk -F"\"" '{ print $1 $4}' | sort -n -r  > artist_by_listens.txt

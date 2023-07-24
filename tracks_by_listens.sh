VAR=${1:-andrew} 
VAR2=${2:-10} 

echo "========================================"
echo "user: $VAR's top $VAR2 tracks by N listens"
echo "========================================"
cat ./$VAR/MyData/StreamingHist*.json | grep "trackName" | sort | uniq -c | awk -F"\"" '{ print $1 $4}' | sort -n -r  > tracks_by_listens.txt

head -$VAR2 tracks_by_listens.txt 

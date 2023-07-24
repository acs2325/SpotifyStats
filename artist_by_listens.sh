VAR=${1:-andrew} 
VAR2=${2:-10} 

echo "========================================"
echo "user: $VAR's top $VAR2 artists by N listens"
echo "========================================"
cat ./$VAR/MyData/StreamingHist*.json | grep "artist" | sort | uniq -c | awk -F"\"" '{ print $1 $4}' | sort -n -r  > artist_by_listens.txt

head -$VAR2 artist_by_listens.txt 

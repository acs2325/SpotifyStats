VAR=${1:-andrew} 
#cat $VAR/MyData/StreamingHistory*.json | sed 's/King Gizzard & The Lizard Wizard/KGATLW/g' | sed 's/\]\[/,/g' | sed 's/\é/e/g' | sed "s/\'//g" | sed 's/\$/S/g' > $VAR/MyData/stream_hist.json
#cat $VAR/MyData/StreamingHistory*.json | sed 's/Beyonc\é/Beyonce/g' | sed 's/King Gizzard & The Lizard Wizard/KGATLW/g' | sed 's/\]\[/,/g' | sed "s/\'//g"  > $VAR/MyData/stream_hist.json
cat $VAR/MyData/StreamingHistory*.json | sed 's/Beyonc\é/Beyonce/g' | sed 's/King Gizzard & The Lizard Wizard/KGATLW/g' | sed 's/\]\[//g' |  sed 's/},/beauthedoggy/g' | sed '0,/\}/{s/\}/\},/}' | sed 's/beauthedoggy/},/g' | sed "s/\'//g"  > $VAR/MyData/stream_hist.json

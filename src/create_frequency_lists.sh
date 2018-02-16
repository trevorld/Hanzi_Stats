cat data/i-zh-char.num.html | tail -n +17 | cut -f3 | xargs -n 500  echo | sed 's/ //g' > simplified_freq.txt

cat data/traditional_frequency.txt | cut -f1 -d" " | xargs -n 500 echo | sed 's/ //g' > traditional_freq.txt

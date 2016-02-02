cat data/i-zh-char.num.html | tail -n +17 | cut -f3 | xargs -n 500  echo | sed 's/ //g' > freq.txt

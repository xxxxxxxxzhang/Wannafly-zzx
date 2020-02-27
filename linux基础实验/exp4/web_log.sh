#!/bin/bash
#统计访问来源主机TOP 100和分别对应出现的总次数
echo "访问来源主机TOP 100和分别对应出现的总次数"
more web_log.tsv | awk -F '\t' '{print $1}'| sort | uniq -c | sort -k1 -nr | head -n 100
echo ""

#访问来源主机TOP 100 IP和分别对应出现的总次数
echo "访问来源主机TOP 100 IP和分别对应出现的总次数"
more  web_log.tsv | awk -F '\t ' '{print $1}' | egrep '[[:digit:]]{1,3}\.[[:digit:]]{1,3}\.[[:digit:]]{1,3}\.[[:digit:]]{1,3}' | sort | uniq -c | sort -nr | head -n 100|awk '{print $2,$1 }'

#统计最频繁被访问的URL TOP 100
echo "最频繁被访问的URL TOP 100"
more +2 web_log.tsv |awk -F '\t ' '{print $5}'|sort|uniq -c |sort -nk1r|head -n 100|awk '{print $2}'
#统计不同响应状态码的出现次数和对应百分比
a=$(more +2 web_log.tsv |awk -F\\t '{print $6}'|sort|uniq -c |sort -n -k 1 -r|head -n 10|awk '{print $1}')
b=$(more +2 web_log.tsv |awk -F\\t '{print $6}'|sort|uniq -c |sort -n -k 1 -r|head -n 10|awk '{print $2}')
sum=0
count=($a)
responsecode=($b)
for i in $a ;do
        sum=$(($sum+$i))
done

i=0
for n in ${count[@]};do
b[$i]=$(echo "scale=2; 100*${n} / $sum"|bc)
  i=$((i+1))
done

echo  "不同响应状态码的出现次数和对应百分比 \n"
i=0
for n in ${count[@]};do
echo -e "${responsecode[$i]} $n ${b[$i]}% \n "
i=$((i+1))
done
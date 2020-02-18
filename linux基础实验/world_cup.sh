#以\t'为分隔符 找到第六行
age=$(awk -F '\t' '{print $6}' worldcupplayerinfo.tsv)
#awk -F '\t' '{print $6}' worldcupplayerinfo.tsv
	sum=0
	age_count1=0
	age_count2=0
	age_count3=0

	for num in $age
	do
	    if [ "$num" != 'Age' ] ; then #去掉第一行
	  		let sum+=1
	
			if [ "$num" -lt 20 ] ; then 
		    	# let age_count1+=1  
		    	age_count1=$((${age_count1}+1))
			fi
	
	  		if [ "$num" -ge 20 ] && [ "$num" -le 30 ] ; then 
		    	let age_count2+=1
	            #echo "age_count2=${age_count2} num=${num}"
			fi
	
	  		if [ "$num" -gt 30 ] ; then 
		    	let age_count3+=1  
			fi
	
	     fi
	done
echo "---------------------------------------------------------"	
echo "年龄统计情况： "
echo "<20岁球员数量:${age_count1} ，所占百分比为$(echo "scale=2; ${age_count1}*100/${sum}" | bc)%"
echo "[20-30]的球员数量:${age_count2} ，所占百分比为$(echo "scale=2; ${age_count2}*100/${sum}" | bc)%"
echo ">30岁的球员数量:${age_count3} ，所占百分比为$(echo "scale=2; ${age_count3}*100/${sum}" | bc)%"

#位置统计
position=$(awk -F '\t' '{print $5}' worldcupplayerinfo.tsv)

position_count_Goalie=0;
position_count_Defender=0
position_count_Midfielder=0
position_count_Forward=0

	for pos in $position
	do
	#echo "pos是:$pos"
	   		if [ "$pos" == 'Forward' ] ; then
	  		let position_count_Forward+=1
 			fi
			if [ "$pos" == 'Midfielder' ] ; then 
		    	# let age_count1+=1  
		    	position_count_Midfielder=$((${position_count_Midfielder}+1))
			fi

      		if [ "$pos" == 'Defender' ]; then 
    	    	let position_count_Defender+=1
                #echo "position_count_Defender=${position_count_Defender}"
    		fi
    
      		if [ "$pos" = 'Goalie' ] ; then 
    	    	let position_count_Goalie+=1  
    		fi


​         
	done
echo "---------------------------------------------------------"
echo "位置统计情况： "
echo "Forward位球员数量:${position_count_Forward} ，所占百分比为$(echo "scale=2; ${position_count_Forward}*100/${sum}" | bc)%"
echo "Midfielder位球员数量:${position_count_Midfielder} ，所占百分比为$(echo "scale=2; ${position_count_Midfielder}*100/${sum}" | bc)%"
echo "Defender位球员数量:${position_count_Defender} ，所占百分比为$(echo "scale=2; ${position_count_Defender}*100/${sum}" | bc)%
echo "Defender位球员数量:${position_count_Goalie} ，所占百分比为$(echo "scale=2; ${position_count_Goalie}*100/${sum}" | bc)%

#名字长短
namelen=$(awk -F '\t' '{print $9}' worldcupplayerinfo.tsv)
IFS=$'\n' namearray=($namelen)
min=999
max=0
mintemp=''
maxtemp=''
for len in ${namearray[*]} 
do
	#echo "len:${len},长度：${#len}"
	if [ ${#len} -lt $min ] ; then
		#echo "min:${min}"
	 	min=${#len}
	 	mintemp=${len}
	 	#echo "mim:${min} 短名字:${len}"
	fi
	if [ ${#len} -gt $max ] ; then
		#echo "max:${max}"
	 	max=${#len}
	 	maxtemp=${len}
	 	#echo "max:${max} 长名字:${maxtemp}"
	fi
	
done
echo "---------------------------------------------------------"
echo "找出最长最短的名字："
echo "最长名字：${maxtemp},长度:${max}"
echo "最短名字：${mintemp},长度：${min}"
#年纪大小
agenum=$(awk -F '\t' '{print $6}' worldcupplayerinfo.tsv)
young=999
old=0

#echo "agenum:${agenum}"

for ages in $agenum
do

	if [ $ages -lt $young ] ; then
		 young=$ages
	fi
	if [ $ages -gt $old ] ; then
		old=$ages
	fi
done

echo "找出最大最小的年龄："
echo "最大：${old}"
echo "最小：${young}"
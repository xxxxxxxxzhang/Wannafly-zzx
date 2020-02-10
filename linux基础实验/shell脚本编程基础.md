# 第四章：shell脚本编程基础

 [https://github.com/CUCCS/linux-2019-jackcily/blob/08e0c9aaead96d33e11d6b5c24d27a12cf7c1463/job4/%E5%AE%9E%E9%AA%8C%E5%9B%9B%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A.md](https://github.com/CUCCS/linux-2019-jackcily/blob/08e0c9aaead96d33e11d6b5c24d27a12cf7c1463/job4/实验四实验报告.md) 

* 任务一：用bash编写一个图片批处理脚本，实现以下功能：
     *  支持命令行参数方式使用不同功能
     *  支持对指定目录下所有支持格式的图片文件进行批处理
      *  支持以下常见图片批处理功能的单独使用或组合使用
         
          * 支持对`jpeg`格式图片进行图片质量压缩
          
            
          
           * 支持对`jpeg/png/svg`格式图片在保持原始宽高比的前提下压缩分辨率
             
               
             
          * 支持对图片批量添加自定义文本水印
          
          * 支持批量重命名（统一添加文件名前缀或后缀，不影响原始文件扩展名）
          
            
          
          * 支持将`png/svg`图片统一转换为`jpg`格式图片
          
            for %f in (*.jpg) do convert “%f” “%~nf.png
          
            for %f in (*.svg) do convert “%f” “%~nf.png
            
            ```bash
            #!/bin/bash
            workDir=`pwd`
            
            # flags
            compress=0
            resize=0
            watermark=0
            rename=0
            convert=0
            
            # args
            watermarkText=""
            renameText=""
            
            usage() {
                echo "Usage:"
                echo "  ch4_task_1.sh [-c] [-r] [-w TEXT] [-R SUFFIX] [-C]"
                echo "Description:"
                echo "  -c 支持对jpeg格式图片进行图片质量压缩"
                echo "  -r 支持对jpeg/png/svg格式图片在保持原始宽高比的前提下压缩分辨率"
                echo "  -w 支持对图片批量添加自定义文本水印"
                echo "  -R 支持批量重命名（统一添加文件名后缀，不影响原始文件扩展名）"
                echo "  -C 支持将png/svg图片统一转换为jpg格式图片"
                exit -1
            }
            
            
            while getopts 'hcrw:R:C' OPT; do
                case $OPT in
                    h) usage;;
                    c) compress=1;;
                    r) resize=1;;
                    w) watermark=1; watermarkText=$OPTARG;;
                    R) rename=1; renameText=$OPTARG;;
                    C) convert=1;;
                    ?) usage;;
                esac
            done
            # shift $(($OPTIND - 1))
            # file=$1
            
            if [ -d "$workDir" ]; then
                for zfile in $(find *.JPG *.jpg *.png *.PNG *.svg *.SVG 2>/dev/null); do
                    if [[ compress -eq 1 ]]; then
                        $(convert ${zfile} -quality 60 ${zfile})
                    fi
                    if [[ resize -eq 1 ]]; then
                        $(convert $zfile -resize 75%x75% ${zfile})
                    fi
                    if [[ watermark -eq 1 ]]; then
                        $(convert $zfile -fill red -pointsize 25 -annotate +50+50 $watermarkText $zfile)
                    fi
                    if [[ rename -eq 1 ]]; then
                        filename=${zfile%%.*}
                        ext=${zfile##*.}
                        $(mv $zfile "${filename}${renameText}.${ext}")
                    elif [[ convert -eq 1 ]]; then
                        filename=${zfile%%.*}
                        $(convert $zfile "${filename}.jpg")
                    fi
                done
            fi
            ```
            
            ```bash
            #!/bin/bash
            #输出帮助信息
            useage()   
            {
              echo "Useage:bash test.sh  -d <directory> [option|option]"
              echo "options:"
              echo "  -d [directory]                想处理文本的文件路径"
              echo "  -c                            png/svg -> jpg"
              echo "  -r|--resize [width*height|width]    保持某个压缩比进行图像压缩 700x700 or 50%x50%   如果输入的是一个数值 就是保持原始纵横比进行压缩"
              echo "  -q|--quality [number]          对jpg图像进行质量压缩"
              echo "  -w|watermark [watermark]       添加水印"
              echo "  --prefix[prefix]               添加前缀"
              echo "  --postfix[postfix]             添加后缀"
            }
            
            while true ; do   
                case "$1" in
                
                    -c) C_FLAG="1" ; shift ;;
                    
                    -r|--resize) R_FLAG="1";
                        case "$2" in
                            "") shift 2 ;;
                            *)RESOLUTION=$2 ; shift 2 ;;
                        esac ;;
                        
                    --help) H_FLAG="1"; shift ;;
                    
                    -d|--directory)
                        case "$2" in 
                            "") shift 2 ;;
                             *) DIR=$2 ; shift 2 ;;
                        esac ;;
                        
                    -q|--quality) Q_FLAG="1";
                        case "$2" in
                            "") shift 2 ;;
                             *) quality=$2; shift 2 ;;  #todo if the arg is integer
                        esac ;;
                        
                    -w|--watermark)W_FLAG="1"; watermark=$2; shift 2 ;;
                    
                    --prefix) PREFIX=$2; shift 2;;
                    
                    --postfix) POSTFIX=$2; shift 2 ;;
                            
                    --) shift ; break ;;
                    *) echo "Internal error!" ; exit 1 ;;
                esac
            done
            useage()   
            ```
            
            

```shell
#!/bin/bash
quality="70"            #图片质量
RESOLUTION="50%x50%"    #图片压缩率
watermark=""            #图片水印
Q_FLAG="0"   			#质量压缩
R_FLAG="0"
W_FLAG="0"				#加水印
C_FLAG="0"				#格式转换
H_FLAG="0"				#帮助信息flag
PREFIX=""
POSTFIX=""
DIR=`pwd`              #要操作的图片目录
# read the options

#输出帮助信息
useage()   
{
  echo "Useage:bash test.sh  -d <directory> [option|option]"
  echo "options:"
  echo "  -d [directory]                想处理文本的文件路径"
  echo "  -c                            png/svg -> jpg"
  echo "  -r|--resize [width*height|width]    保持某个压缩比进行图像压缩 700x700 or 50%x50%   如果输入的是一个数值 就是保持原始纵横比进行压缩"
  echo "  -q|--quality [number]          对jpg图像进行质量压缩"
  echo "  -w|watermark [watermark]       添加水印"
  echo "  --prefix[prefix]               添加前缀"
  echo "  --postfix[postfix]             添加后缀"
}

main()
{
#输出帮助信息
if [[ "$H_FLAG" == "1" ]]; then
    useage
fi
#-d dir 如果是文件夹返回true
if [ ! -d "$DIR" ] ; then
  echo "No such directory"
  exit 0
fi

#在dir下新建一个output输出文件
output=${DIR}/output
mkdir -p $output

#首先拼凑出需要执行的指令
command="convert"
IM_FLAG="2"
#如果需要进行压缩
if [[ "$Q_FLAG" == "1" ]]; then
  IM_FLAG="1"
  command=${command}" -quality "${quality}
fi
#如果需要进行压缩   需要查一下convert函数的压缩参数的输入
if [[ "$R_FLAG" == "1" ]]; then
  command=${command}" -resize "${RESOLUTION}
fi
#如果需要添加水印
if [[ "$W_FLAG" == "1" ]]; then
  echo ${watermark}
  command=${command}" -fill white -pointsize 40 -draw 'text 10,50 \"${watermark}\"' "
fi

#如果需要转换格式
if [[ "$C_FLAG" == "1" ]]; then
  IM_FLAG="2"
fi

#根据需要获取对应后缀的图片  imgs中存储的是绝对路径
case "$IM_FLAG" in
       1) images=`find $DIR -maxdepth 1 -regex '.*\(jpg\|jpeg\)'` ;;
       2) images=`find $DIR -maxdepth 1 -regex '.*\(jpg\|jpeg\|png\|svg\)'` ;;
esac 

#根据指令处理每一个文件
for CURRENT_IMAGE in $images; do
     filename=$(basename "$CURRENT_IMAGE")  #只取出文件名  .2.jpeg
     name=${filename%.*}                    #去掉后缀    .2
     suffix=${filename#*.}                  #取出后缀     .jpeg
     if [[ "$suffix" == "png" && "$C_FLAG" == "1" ]]; then 
       suffix="jpg"
     fi
     if [[ "$suffix" == "svg" && "$C_FLAG" == "1" ]]; then
       suffix="jpg"
     fi
     savefile=${output}/${PREFIX}${name}${POSTFIX}.${suffix}  #重新拼出一个存储路径
     temp=${command}" "${CURRENT_IMAGE}" "${savefile}  #指令 需要执行操作的图片路径  图片操作后存储路径
     
     #运行拼凑出来的指令
     eval $temp     
     echo $temp
done

exit 0

}
# $@指代命令行上的所有参数
# -o 后面接短参数  没有冒号:开关指令 一个冒号:需要参数  两个冒号:参数可选
# -o cr:d:q:w:   c是可选参数 其他都必须跟一个选项值
# -l 后面接长选项列表
# -n 指定那=哪个脚本处理的这个参数

TEMP=`getopt -o cr:d:q:w: --long quality:arga,directory:,watermark:,prefix:,postfix:,help,resize: -n 'test.sh' -- "$@"`
# -- 保证后面的字符串不直接被解析
#set会重新排列参数顺序 这些值在 getopt中重新排列过了
eval set -- "$TEMP"
#shift用于参数左移 shift n 前n位都会被销毁
while true ; do   
    case "$1" in
    
        -c) C_FLAG="1" ; shift ;;
        
        -r|--resize) R_FLAG="1";
            case "$2" in
                "") shift 2 ;;
                *)RESOLUTION=$2 ; shift 2 ;;
            esac ;;
            
        --help) H_FLAG="1"; shift ;;
        
        -d|--directory)
            case "$2" in 
                "") shift 2 ;;
                 *) DIR=$2 ; shift 2 ;;
            esac ;;
            
        -q|--quality) Q_FLAG="1";
            case "$2" in
                "") shift 2 ;;
                 *) quality=$2; shift 2 ;;  #todo if the arg is integer
            esac ;;
            
        -w|--watermark)W_FLAG="1"; watermark=$2; shift 2 ;;
        
        --prefix) PREFIX=$2; shift 2;;
        
        --postfix) POSTFIX=$2; shift 2 ;;
                
        --) shift ; break ;;
        *) echo "Internal error!" ; exit 1 ;;
    esac
done
main
#todo  检查参数类型
```

查看图片大小`indentify`：

![](img/compare-large.png)

shift命令用于对参数的移动（左移），通常用于再不知道传入参数的情况下遍历灭一个参数然后进行相应的处理

例如：

```bash
#!/usr/bin/env bash

while [ $# != 0 ];do
echo "第一个参数为：$1,参数个数为：$#"
shift
done
```

 输入如下命令运行：run.sh a b c d e f 

结果：

![](img/shift.png)



 getopt命令可以接受一系列任意形式的命令行选项和参数，并自动将它们转换成适当的格式。格式如下： 

` getopt optstring parameters `

* 任务二：用bash编写一个文本批处理脚本，对以下附件分别进行批量处理完成相应的数据统计任务： 
  * 2014世界杯运动员数据
    * 统计不同年龄区间范围（20岁以下、[20-30]、30岁以上）的球员**数量**、**百分比**
    * 统计不同场上位置的球员**数量**、**百分比**
    * 名字最长的球员是谁？名字最短的球员是谁？
    * 年龄最大的球员是谁？年龄最小的球员是谁？

```shell
#!/bin/bash

age_count()
{
#从第二行开始读取
#gawk -F：'{print $1}' /etc/passwd -F也是用来设定读入文件分割符为“:”
#sort按照倒序进行排序
#BEGIN模式指定处理文本前需要执行的操作，END模式指定了处理完所有的行之后所要执行的操作
#读取文件将文件分开
a=$(more +2  job4/worldcupplayerinfo.tsv|awk -F\\t '{print $6}'|sort -r|awk 'BEGIN{split("<20 20-30 >30",b)}{if($1<20)a[1]++;if($1>=20&&$1<=30)a[2]++;if($1>30)a[3]++}END{for(i in a)print a[i]}')

#计算出总人数
sum=0
age=($a)
for i in $a ;do
   sum=$(($sum+$i)) 
done

#计算出百分比
a=("<20" "20-30" ">30")
for i in `seq 0 2`;do
b[$i]=$(echo "scale=2; 100*${age[$i]} / $sum"|bc)
done

echo -e "------统计不同年龄区间范围------"
for i in `seq 0 2`;do
echo -e "${a[$i]}  人数: ${age[$i]} 百分比: ${b[$i]}% \n "
done
}


#uniq -c函数使用之前 使用 sort 命令使所有重复行相邻
pos_count()
{
	a=$(more +2 job4/worldcupplayerinfo.tsv|awk -F\\t '{print $5}'|sort -r|uniq -c|awk '{print $1}')
	b=$(more +2 job4/worldcupplayerinfo.tsv|awk -F\\t '{print $5}'|sort -r|uniq -c|awk '{print $2}')
	sum=0
	count=($a)
	position=($b)

    #求和用于计算百分比
	for i in $a ;do
		sum=$(($sum+$i)) 
	done

#遍历计算百分比
i=0
for n in ${count[@]};do
b[$i]=$(echo "scale=2; 100*${n} / $sum"|bc)
  i=$((i+1))
done

#进行输出打印
echo -e "----统计不同场上位置的球员数量、百分比------"
i=0
for n in ${count[@]};do
echo -e "位置: ${position[$i]}  数量: $n   百分比: ${b[$i]}% \n " 
i=$((i+1))
done
}


young()
{
#首先找出年龄最小的数值
young=$(more +2 job4/worldcupplayerinfo.tsv | awk -F\\t 'BEGIN{young=100}{if($6<=young){young=$6}}END{print young}')

#然后把所有年龄为该数值的名字取出
temp="more +2 job4/worldcupplayerinfo.tsv | awk -F'\t' 'BEGIN{young="${young}";i=1}{if("'$6'"==young){name[i]="'$9'";i++}}END{for (a in name)print name[a]}'"

name=$(eval -- $temp)

echo -e "------年龄最小的球员是谁------\n"

echo -e "最小的年龄是: ${young} "
echo -e "名字是 : \n"
IFS=$'\n' namearray=($name)
for key in "${!namearray[@]}"; do echo "${namearray[$key]}"; done


}

old()
{
#计算方式和计算最小的年龄类似
old=$(more +2 job4/worldcupplayerinfo.tsv | awk -F\\t 'BEGIN{old=0}{if($6>=old){old=$6}}END{print old}')

temp="more +2 job4/worldcupplayerinfo.tsv | awk -F'\t' 'BEGIN{old="${old}";i=1}{if("'$6'"==old){name[i]="'$9'";i++}}END{for (a in name)print name[a]}'"


name=$(eval -- $temp)

echo -e "------年龄最大的球员是谁------\n"
echo -e "最大年龄: ${old} "
echo -e "名字是 : \n"

IFS=$'\n' namearray=($name)
for key in "${!namearray[@]}"; do echo "${namearray[$key]}"; done


}

longgest_name()
{

name=$(more +2 job4/worldcupplayerinfo.tsv | awk -F\\t '{print $9}') 
long=0
IFS=$'\n' namearray=($name)

#首先求出名字最长的数值是多少
for i in ${namearray[*]} ; do
  count=$(echo -n $i | wc -m )
  if [ $count -gt $long ] ; then
    long=$count
  fi
done

#然后遍历寻找长度符合条件的名字
num=0
longarray=()
for i in ${namearray[*]} ; do
  count=$(echo -n $i | wc -m)
  if [ $count -eq $long ] ; then
    longarray[${num}]=$i
    num=$((num+1))
  fi
done

echo -e "------最长的名字是-----  \n"
echo -e "最长的名字长度: ${long} "
echo -e "名字是: \n"

for key in "${!longarray[@]}"; do echo "${longarray[$key]}"; done

}

#求解原理同上
shortest_name()
{

name=$(more +2 job4/worldcupplayerinfo.tsv | awk -F\\t '{print $9}') 
short=100
IFS=$'\n' namearray=($name)

for i in ${namearray[*]} ; do
  count=$(echo -n $i | wc -m )
  if [ $count -lt $short ] ; then
    short=$count
  fi
done

num=0
shortarray=()
for i in ${namearray[*]} ; do
  count=$(echo -n $i | wc -m)
  if [ $count -eq $short ] ; then
    shortarray[${num}]=$i
    num=$((num+1))
  fi
done

echo -e "------最短名字数据------  \n"

echo -e "最短名字长度: ${short} "
echo -e "名字是 : \n"

for key in "${!shortarray[@]}"; do echo "${shortarray[$key]}"; done

}

age_count
pos_count
longgest_name
shortest_name
old
young

```



```shell
#!/bin/bash

function age_stats
{
	age=$(awk -F '\t' '{print $6}' worldcupplayerinfo.tsv)
	sum=0
	a=0
	b=0
	c=0

	for n in $age
	do
	    if [ "$n" != 'Age' ] ; then
      		let sum+=1

		if [ "$n" -lt 20 ] ; then 
		    let a+=1  
		fi

      		if [ "$n" -ge 20 ] && [ "$n" -le 30 ] ; then 
		    let b+=1  
		fi

      		if [ "$n" -gt 30 ] ; then 
		    let c+=1  
		fi

            fi
	done

	ratio1=$(awk 'BEGIN{printf "%.3f",'"$a"*100/"$sum"'}')
	ratio2=$(awk 'BEGIN{printf "%.3f",'"$b"*100/"$sum"'}')
	ratio3=$(awk 'BEGIN{printf "%.3f",'"$c"*100/"$sum"'}')

	echo "---------------- # Age Statistics # --------------------"
	echo "--------------------------------------------------------"
	echo "|    Age     |    < 20    |    20 ~ 30    |    > 30    |"
	echo "--------------------------------------------------------"
	echo "|Total Number|     "$a"      |      "$b"      |    "$c"     |"
	echo "--------------------------------------------------------"
	echo "| Proportion |   "$ratio1" "%"  |    "$ratio2" "%"   |  "$ratio3" "%"  |"
	echo "--------------------------------------------------------" 


	temp=$(sort -k6 worldcupplayerinfo.tsv| awk -F'\t' '{print $6 "\t" $9}'|head > target.txt)
 	min_names=$(more target.txt | awk -F'\t' 'BEGIN{min=100;i=1}{if(min>=$1){min=$1;name[i++]=$2}}END{for(n in name)print name[n]}')
	min=$(more target.txt | awk -F'\t' 'BEGIN{min=100;i=1}{if(min>=$1){min=$1}}END{print min}')
	echo "---- # the youngest players ("$min") # ----"
	echo "$min_names"

	temp=$(sort -k6 -nr worldcupplayerinfo.tsv| awk -F'\t' '{print $6 "\t" $9}'|head > target1.txt)
	max_names=$(more target1.txt | awk -F'\t' 'BEGIN{max=0;i=1}{if(max<=$1){max=$1;name[i++]=$2}}END{for(n in name)print name[n]}')
	max=$(more target1.txt | awk -F'\t' 'BEGIN{max=0;i=1}{if(max<=$1){max=$1}}END{print max}')
	echo "---- # the oldest players ("$max") # ----"
	echo "$max_names"
}


function position_stats
{	
	num=$(sed -n '2, $ p' worldcupplayerinfo.tsv|awk -F '\t' '{print $5}'|sort -r|uniq -c|awk '{print $1}')
	position=$(sed -n '2, $ p' worldcupplayerinfo.tsv|awk -F '\t' '{print $5}'|sort -r|uniq -c|awk '{print $2}')
	n=($num)
	p=($position)
        
	sum=0
	
	for i in $num
	do
	    let sum+=$i
	done

	i=0

	for n in ${num[@]}
	do
	    b["$i"]=$(echo "scale=3; 100*$n / $sum "|bc)

 	    i=$((i+1))
	done
	

	echo "---------- # Position Statistics # --------------"
	echo "-------------------------------------------------"	


	i=0
	p=($position)
	n=($num)
	
	for k in $(seq 0 $(echo "${#n[@]}-1"|bc))
	do
	    echo "Position: ${p[$i]}"
	    echo "Number: ${n[$i]} "
	    echo "Proportion: ${b[$i]} %"
	    let i+=1
	done
}

function name_stats
{
	longest=$(awk -F'\t' 'BEGIN{max=0}{if(length($9)>max){max=length($9);}}END{print max}' worldcupplayerinfo.tsv)
	long_names=$(awk -F'\t' 'BEGIN{longest='$longest';i=1}{if(length($9)==longest){name[i++]=$9}}END{for(n in name)print name[n]}' worldcupplayerinfo.tsv)
	shortest=$(awk -F'\t' 'BEGIN{min=100}{if(length($9)<min){min=length($9);}}END{print min}' worldcupplayerinfo.tsv)
        short_names=$(awk -F'\t' 'BEGIN{shortest='$shortest';i=1}{if(length($9)==shortest){name[i++]=$9}}END{for(n in name)print name[n]}' worldcupplayerinfo.tsv)
	
	echo "---- # the players whose name is longest ($longest) ----"
        echo "${long_names}"

	echo "--- # the players whose name is shortest ($shortest) ---"
        echo "${short_names}"


}

function main
{
age_stats
echo -e
echo -e
position_stats
echo -e
echo -e
name_stats
}

main


```



任务二：用bash编写一个文本批处理脚本，对以下附件分别进行批量处理完成相应的数据统计任务： 

- Web服务器访问日志
  - 统计访问来源主机TOP 100和分别对应出现的总次数
  - 统计访问来源主机TOP 100 IP和分别对应出现的总次数
  - 统计最频繁被访问的URL TOP 100
  - 统计不同响应状态码的出现次数和对应百分比
  - 分别统计不同4XX状态码对应的TOP 10 URL和对应出现的总次数
  - 给定URL输出TOP 100访问来源主机

```shell
#!/bin/bash
url="/"

#统计不同的host
host_top()
{
echo -e "统计访问来源主机TOP 100和分别对应出现的总次数 \n"
more +2 web_log.tsv | awk -F\\t '{print $1}' |  sort | uniq -c | sort -nr | head -n 100|awk '{print $2,$1}'


exit 0
}

#统计不同的ip 使用正则匹配ip   是指统计ip的意思吗
ip_top()
{
echo -e  "统计访问来源主机TOP 100 IP和分别对应出现的总次数 \n"
more +2 web_log.tsv | awk -F\\t '{print $1}' | egrep '[[:digit:]]{1,3}\.[[:digit:]]{1,3}\.[[:digit:]]{1,3}\.[[:digit:]]{1,3}' | sort | uniq -c | sort -nr | head -n 100|awk '{print $2,$1}'
exit 0
}

#直接排序
frequency_url_top()
{
#统计最频繁被访问的URL TOP 100
echo -e "统计最频繁被访问的URL TOP 100 \n"
more +2 web_log.tsv |awk -F\\t '{print $5}'|sort|uniq -c |sort -n -k 1 -r|head -n 100|awk '{print $2}'
exit 0
} 



responsecode_stat()
{
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

echo -e "------响应码数据----------  \n"
i=0
for n in ${count[@]};do
echo -e "${responsecode[$i]} $n ${b[$i]}% \n " 
i=$((i+1))
done

exit 0
}


#4xxURL状态码对应的TOP 10 URL和对应出现的总次数
responsecode_top()
{

echo -e "4xxURL状态码对应的TOP 10 URL和对应出现的总次数 \n"
right=500
left=399

#首先过滤出所有4xx状态
a=$(more +2 web_log.tsv |awk -F\\t '{print $6}'|sort|uniq -c |awk '{print $2}')

#这个时候拿到了所有的响应码的数组
count=($a)

#进行循环遍历 如果是4xx 就进行抓取 否则不作处理
i=0
for n in ${count[@]};do
	if [ $n -lt $right ]&&[ $n -gt $left ]  #如果这个取值是4xx
 then
   echo ${n}      #响应码  url
   #怎么拼接字符串
   more +2 web_log.tsv |awk -F\\t '{print $6,$5}' | grep ${n}" " |sort|uniq -c |sort -n -k 1 -r|head -n 10|awk '{print $3,$1}'
 fi
done


exit 0
}


url_host()
{
url="	"$url"	"
echo -e "给定URL输出TOP 100访问来源主机 \n"
temp="more +2 web_log.tsv |grep \""'${url}'"\"|awk -F'\t' '{print "'$1'"}'|sort|uniq -c|sort -nr|head -n 10"
#echo $temp

eval -- $temp
exit 0
}



useage()
{
	echo "Usage: bash test3.sh [OPTION]"

	echo "-a				show TOP 100 host and count"
	echo "-b 				show TOP 100 IP and count"
	echo "-c 				show TOP 100 frequency url and count"
	echo "-d 				show responsecode and count and porprotion"
	echo "-e 				show TOP 10 4XX responsecode  url and count"
	echo "-f [url]			show TOP 100 given url of host and count"	
	exit 0
}


option=`getopt -o a,b,c,d,e,f: --long help -n 'test.sh' -- "$@"`

eval set -- "$option"

while true; do
	case "$1" in 
		-a) host_top ;shift ; break;;
        -b) ip_top ; shift ; break;;
		-c) frequency_url_top ; shift ; break;;
		-d) responsecode_stat ; shift ; break;;
		-e) responsecode_top ; shift ; break;;
		-f) url=$2 ; url_host; shift ; break ;;
     	--help) useage ; shift ; break ;;
        --)shift; break ;;
 		*) echo "Internal error! see --help for more information"; exit 1 ;;
	esac
done

```

```shell
# Top 100

echo "------ # Top 100 hosts and according frequencies # -------"
echo -e
top100Host=$(more web_log.tsv | awk -F '\t' '{print $1}'| sort | uniq -c | sort -k1 -nr | head -n 100)
echo "$top100Host"


echo "---- # Top 100 hosts' IP and according frequencies # -----"
echo -e
top100IP=$(more web_log.tsv | awk -F '\t' '{print $1}' | egrep '[[:digit:]]{1,3}\.[[:digit:]]{1,3}\.[[:digit:]]{1,3}\.[[:digit:]]{1,3}' | sort | uniq -c | sort -k1 -nr | head -n 100)
echo "$top100IP"


echo "--- # Top 100 busiest URLs and according frequencies # ---"
echo -e
top100URL=$(more web_log.tsv |awk -F '\t' '{print $5}' | sort | uniq -c | sort -k1 -nr | head -n 100)
echo "$top100URL"

function RespStats
{

	respCode=$(sed -n '2,$ p' web_log.tsv |awk -F'\t' '{print $6}'| sort | uniq -c | sort -nr | head -n 10 | awk '{print $2}')

	respCount=$(sed -n '2,$ p' web_log.tsv |awk -F'\t' '{print $6}'| sort | uniq -c |sort -nr | head -n 10 | awk '{print $1}')

	code=($respCode)
	count=($respCount)

	sum=0
	 for i in $respCount
	 do
		sum=$((${sum}+${i}))
	done

	p=0
	for k in ${count[@]}
	do	
		ratio[${p}]=$(echo "scale=4; 100*${k}/$sum"|bc)
		let p+=1
	done
	
	echo -e
	echo -e "----- # Response Code Statistics # -----"
	echo "----------------------------------------"
	echo -e
	for i in $(seq 0 $(echo "${#count[@]}-1"|bc))
	do
		echo "Response Code: "${code[${i}]}" "
		echo "Response Count: "${count[${i}]}" "
		echo "Proportion: "${ratio[${i}]}" %"
	done
	echo -e


	# Top10 Url Over 4xx
	# Top1/our/lover/4xx

	temp=$(more web_log.tsv | awk -F'\t' '{if(substr($6,1,1)==4)print $5"\t"$6}' > target2.txt)
	codes_type=$(more target2.txt | awk -F'\t' '{print $2}'| sort | uniq -c | awk '{print $2}')
	codes_count=$(more target2.txt | awk -F'\t' '{print $2}'| sort | uniq -c | awk '{print $1}')

	# 404 403
	for t in $codes_type
	do	
		
		echo -e "-------# Top 10 urls for response code $t # -------"
		echo -e
		echo "| Frequency |"
		echo -e
		url=$(more target2.txt | awk -F'\t' '{if($2=='$t')print $1}' | sort | uniq -c | sort -nr | head)	
		echo "$url"
		echo -e
	done
	
	

	# Specify a url then find out top 100 hosts ( non-interactive )
	
	url="/images/NASA-logosmall.gif"
	
	echo -e
	echo "----- # Top 100 hosts which visited "$url" # ------"
	echo -e
	echo "| frequency |"
	echo -e 
	hosts=$(more web_log.tsv | awk -F'\t' '{if("'$url'"==$5)print $1}' | sort | uniq -c | sort -k1 -nr |head -n 100)
	echo "$hosts"

	
}

RespStats

```



## 参考

[awk](http://www.zsythink.net/archives/1336)
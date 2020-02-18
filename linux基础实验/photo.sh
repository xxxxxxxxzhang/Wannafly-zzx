#!/bin/bash
quality="70"            #图片质量
RESOLUTION="50%x50%"    #图片压缩率

#flag
Q_FLAG=0   				#质量压缩
R_FLAG=0
W_FLAG=0				#加水印
C_FLAG=0				#格式转换
H_FLAG=0				#帮助信息flag

watermark=""            #图片水印
PREFIX=""				#前缀
POSTFIX=""

DIR=`pwd`              #要操作的图片目录
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
main(){
  #echo "main 函数"
  #echo "H_FLAG:$H_FLAG"
if [ $H_FLAG == 1 ] ; then 
  #echo "Help"
  useage
fi

if [ ! -d "$DIR" ] ;then
  #echo "没有这个路径"
  exit 0
fi

#再目录下建一个目录来保存处理好的图片输出
outimg=${DIR}/outimg
mkdir -p $outimg

command="convert"
IM_FLAG="2"
if [ $Q_FLAG == 1 ] ; then 
  IM_FLAG="1" # 
  command=${command}" -quality "${quality}
fi
if [ $R_FLAG == 1 ] ; then 
  #echo "保持原始宽高比的前提下压缩分辨率";
  command=${command}" -resize "${RESOLUTION}
fi
if [ $W_FLAG == 1 ] ; then 
  #echo "加水印:${watermark}" 
  command=${command}" -fill white -pointsize 40 -draw 'text 10,50 \"${watermark}\"' "
fi

if [ $C_FLAG == 1 ] ; then 
  IM_FLAG="2"
  #echo "转换格式"
fi


case "$IM_FLAG" in
       1) images=`find $DIR -maxdepth 1 -regex '.*\(jpg\|jpeg\)'` ;;
       #路径 深度 1 正则表达式
       2) images=`find $DIR -maxdepth 1 -regex '.*\(jpg\|jpeg\|png\|svg\)'` ;;
esac
#根据指令处理每一个图片
for CURRENT_IMAGE in $images; do
     filename=$(basename "$CURRENT_IMAGE")  #只取出文件名  .2.jpeg
     name=${filename%.*}                    #去掉后缀    .2
     suffix=${filename#*.}                  #取出后缀     .jpeg
     if [[ "$suffix" == "png" && $C_FLAG == 1 ]]; then 
       suffix="jpg"
     fi
     if [[ "$suffix" == "svg" && $C_FLAG == 1 ]]; then
       suffix="jpg"
     fi
     savefile=${outimg}/${PREFIX}${name}${POSTFIX}.${suffix}  #重新拼出一个存储路径，图片类型
     temp=${command}" "${CURRENT_IMAGE}" "${savefile}  #指令 需要执行操作的图片路径  图片操作后存储路径
     
     #运行拼凑出来的指令
     eval $temp     
     #echo $temp
done
exit 0
}
#-o表示短选项，两个冒号表示该选项有一个可选参数，可选参数必须紧贴选项
#如-carg 而不能是-c arg
#--long表示长选项
#"$@"指代命令行上的所有参数
# -n:出错时的信息
# -- ：举一个例子比较好理解：
#我们要创建一个名字为 "-f"的目录你会怎么办？
# mkdir -f #不成功，因为-f会被mkdir当作选项来解析，这时就可以使用
# mkdir -- -f 这样-f就不会被作为选项。
#getops和getopt的冒号作用是不一样的： 一. 对于getops 1. 第一个字符是冒号，表面忽略错误信息 2. 字母后面的单冒号，表示带参数，不带也行（只有最后一个选项才可以不带参数） 3. 字母后面的双冒号，表示强制带参数，不带参数报错

TEMP=`getopt -o cr:d:q:w: --long quality:arga,directory:,watermark:,prefix:,postfix:,help,resize: -n 'test.sh' -- "$@"`
#set 会重新排列参数的顺序，也就是改变$1,$2...$n的值，这些值在getopt中重新排列过了
eval set --"$TEMP";
#echo "命令：$TEMP"

while true ; do   
    case "$1" in
        -c) C_FLAG=1 ; 
        shift ;;
        -d|--directory)
        	case "$2" in
        		"") shift 2 ;;
             *) DIR=$2 ; shift 2 ;;	 
          esac;;    
        -q|--quality) Q_FLAG="1";
            case "$2" in
                "") shift 2 ;;
                 *) quality=$2; shift 2 ;;  #todo if the arg is integer
            esac ;;

        --help) H_FLAG=1;
        -r|--resize) R_FLAG=1; echo "R_FLAG=$R_FLAG";
          	case "$2" in
                "") shift 2 ;;
                *)RESOLUTION=$2 ; shift 2 ;;
            esac ;;
    
        -w) W_FLAG=1;
         	case "$2" in
         		"") shift;;
         		*) watermark=$2;echo "水印：${2}";shift 2;;
            esac;;
    
        --prefix) PREFIX=$2;shift 2;;
    
        --postfix) POSTFIX=$2;shift 2;;
    
        --) shift ; break;;
    
        *) echo "Internal error!" ; exit 1;;
    esac
done
main
#todo
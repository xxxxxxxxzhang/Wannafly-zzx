# shell脚本编程基础

##### 什么是shell脚本

 **Shell Script**  ，Shell脚本与Windows/Dos下的[批处理](https://baike.baidu.com/item/批处理/1448600)相似，也就是用各类命令预先放入到一个文件中，方便一次性执行的一个[程序文件](https://baike.baidu.com/item/程序文件/10510952)，主要是方便管理员进行设置或者管理用的。但是它比Windows下的批处理更强大，比用其他编程[程序编辑](https://baike.baidu.com/item/程序编辑)的程序效率更高，它使用了Linux/Unix下的命令。 

 shell script是利用shell的功能所写的一个程序，这个程序是使用[纯文本文件](https://baike.baidu.com/item/纯文本文件)，将一些shell的语法与指令写在里面，然后用正规表示法，管道命令以及数据流重导向等功能，以达到我们所想要的处理目的。 

##### 给脚本传参

```shell
#!/bin/bash
# 将本段代码复制粘贴保存为一个文件，假设文件名为：test.sh
echo $3 # --> results with: banana

BIG=$5

echo "A $BIG costs just $6"

# 输出所有参数
echo "$@"

# 以下代码输出命令行参数的总数
echo $#
```

```
执行此命令的结果:bash test.sh apple 5 banana 8 "Fruit Basket" 15
```

` 执行结果：banana A "Fruit Basket" costs just 15 apple 5 banana 8 "Fruit Basket" 15 8` 

#### 数组

* 关联数组和索引数组

关联数组和常规说的数组类似，它包含标量数据，可用索引值来单独选择这些数据，和常规数组不同的是， 关联数组的索引值不是非负的整数而是任意的标量。这些标量称为Keys，可以在以后用于检索数组中的数值。 



Bash提供一维索引和关联数组变量。任何变量都可以用作索引数组;declare  builtin将显式地声明一个数组。数组的大小没有最大限制，也没有要求成员被索引或分配为连续的。索引数组使用整数(包括算术表达式(参见外壳算法))进行引用，并且是从零开始的;关联数组使用任意字符串。除非另有说明，索引数组索引必须是非负整数。如果有任何变量是assig，就会自动创建一个索引数组 。

 如果使用该语法指定了任何变量，则会自动创建索引数组 

##### 示例

```shell
# 查看当前 Bash 的 declare 支持的参数
# help declare

# 声明一个「索引」数组
declare -a indexed_arr

# 声明一个「关联」数组
declare -A associative_arr

# Bash 数组赋值方法如下
# 「索引」数组可以跳过数组声明直接赋值的同时即完成了数组初始化
my_array=(apple banana "Fruit Basket" orange)

associative_arr['hello']='world'
associative_arr['well']='done'

# bash支持“稀疏”数组：即数组元素不必连续存在，个别索引位置上可以有未初始化的元素
new_array[2]=apricot

# 数组元素的个数通过 ${#arrayname[@]} 获得
echo ${#my_array[@]}

# 随机读取数组中的元素，{}是必须有的
echo ${my_array[2]}
# echo $my_array[2] 是错误的读取方法

# 遍历数组的方法
## 「索引」数组
for ele in "${my_array[@]}";do
    echo "$ele"
done

## 「关联」数组
for key in "${!associative_arr[@]}";do
    echo "$key ${associative_arr[$key]}"
done
```

#####  测试

```shell
#!/bin/bash
NAMES=( John Eric Jessica )

# 代码填空，使得以下代码避免输出failed关键字
NUMBERS=(seq 1 10) # 构造包含1到10整数的数组
STRINGS=(hello world)  # 构造分别包含hello和world字符串的数组
NumberOfNames=0 # 请使用动态计算数组元素个数的方法
second_name=''  # 读取NAMES数组的第2个元素值进行赋值

# 测试代码 - 勿修改

T_NUMBERS=$(seq 1 10)
T_STRINGS=(hello world)

# Test Case 1
i=0
for n in ${T_NUMBERS[@]};do
  if [[ ${n} -ne ${NUMBERS[${i}]} ]];then
    echo "failed in NUMBERS test"
  fi
  i=$((i+1))
done

# Test Case 2
i=0
for n in ${T_STRINGS[@]};do
  if [[ "${n}" != "${STRINGS[${i}]}" ]];then
    echo "failed in STRINGS test"
  fi
  i=$((i+1))
done

# Test Case 3
if [[ $NumberOfNames -ne ${#NAMES[@]} ]];then
    echo "failed in NumberOfNames test"
fi

# Test Case 4
if [[ "${NAMES[1]}" != "${second_name}" ]];then
  echo "failed in Array Element Access test"
fi
```

##### 条件判断

```shell
# 以下代码执行完毕后的输出结果是什么？
if [[ 0 ]];then printf "%d" 0;fi  
if [[ 1 ]];then printf "%d" 1;fi 1
if [[ true ]];then printf "%d" 2;fi 2
if [[ false ]];then printf "%d" 3;fi 
if [[ '' ]];then printf "%d" 4;fi 
if [[ '   ' ]];then printf "%d" 5;fi
if [[ 'true' ]];then printf "%d" 6;fi
if [[ 'false' ]];then printf "%d" 7;fi
if [[ '$mamashuozhegebianliangbukenengdingyiguo' ]];then printf "%d" 8;fi 
if [[ "$mamashuozhegebianliangbukenengdingyiguo" ]];then printf "%d" 9;fi
```

##### 编写健壮的 shell 脚本

* Fail-Fast: 避免错误蔓延（软件开发中的失败与失败原则）

  人倾向于犯错误，而软件倾向于存在错误。没有错误的唯一代码是从未编写的代码。

  那我们该怎么办呢？

  防止某些事物失败而无法解决任何问题。它不能解决问题，而只是隐藏问题。而且问题出现在表面的时间越长，修复起来就越困难，成本也就越高。

  实际上，系统故障和软件崩溃并不是最严重的情况，有时甚至一点也不坏。更糟的是：死锁，原始错误发生很长时间后崩溃，数据丢失和损坏以及数据不一致。如果系统的一部分发生故障或应用程序在这些更糟的事情发生之前崩溃了，那么我们很幸运。

  这就是为什么**快速失败**原则会鼓励我们快速尽早地失败：如果发生错误，则立即而有目的地失败。如果出现异常或意外情况，请立即使软件发生故障，而不是推迟故障或解决故障。

  **set -e**

  > 脚本只要发生错误，就终止执行

  **set +e**

  > 关闭 -e 选项

  ------

  **set -o pipefail**

  - ```
    set -e
    ```

     不能终止管道命令中执行出错的语句 

    - 只要最后一个子命令不失败，管道命令总是会执行成功

  - `set -eo pipefail` 可以让脚本在更严格的条件下执行

##### 函数

函数定义

```shell
# 基本定义方法，可移植性最好
function_name () compound-command [ redirections ]

# 现代主流shell解释权均支持的语法，可以避免alias机制污染函数名
```

**alias机制**

 [linux系统](https://www.baidu.com/s?wd=linux系统&tn=24004469_oem_dg&rsv_dl=gh_pl_sl_csd)下给命令指定别名alias命令用法: 
 在linux系统中如果命令太长又不符合用户的习惯，那么我们可以为它指定一个别名。虽然可以为命令建立“链接”解决长文件名的问题，但对于带命 令行参数的命令，链接就[无能为力](https://www.baidu.com/s?wd=无能为力&tn=24004469_oem_dg&rsv_dl=gh_pl_sl_csd)了。而指定别名则可以解决此类所有问题。只要举一些例子就可以了： 
 alias l='ls -l' ;用 l 代替 ls -l 命令(Xenix 下就有类似的 l 命令) 
 alias cd..='cd ..' ;用 cd.. 代替 cd .. 命令(对在 DOS 下使用惯了 cd.. 的人帮助很大) 
 alias md='mkdir' ;用 md 代替 mkdir 命令(对在 DOS 下…) 
 alias c:='mount /dev/hda1 /mnt/c & cd /mnt/c' ;用 c: 命令代替命令序列：安装 DOS 分区，再进入。 
 通常我们可以将以上命令放到自己的home目录下的.bash_prifle文件中,在使用source .bash_profile 命令.即可使用. 

函数调用、传参和参数处理

```bash
function function_B {
  echo "Function B."
}
function function_A {
  echo "$1"
}
function adder {
  echo "$(($1 + $2))"
}

# 调用函数，传参
function_A "Function A."     # Function A.
function_B                   # Function B.
adder 12 56                  # 68
```





# 参考

[Shell脚本编程30分钟入门]( https://github.com/qinjx/30min_guides/blob/master/shell.md )
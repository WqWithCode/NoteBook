#Linux指令

##常用指令
###ls　　        显示文件或目录

     -l           列出文件详细信息l(list)

     -a          列出当前目录下所有文件及目录，包括隐藏的a(all)

###mkdir         创建目录
>mkdir [选项] [目录]

     -m   --mode=模式，建立目录的时候同时设置目录的权限；
     -p   --parents 若所建立的上层目录目前尚未建立，则会一并建立上层目录；
     -v   --verbose 每次创建新目录都显示信息
     -h   --help 帮助信息
>文件和目录的权限表示，是用rwx这三个字符来代表所有者、用户组和其他用户的权限。     
>通常这三个用户可表示为ugo
````
u = user
g = group
o = other
````
>因为每个用户有rwx三个对应权限，而我们只要把这三个权限用0或者1表示，如000，110，
>再转换成10进制表示，111=7，然后三种用户的权限排列起来，如700，,755,等，
>按照rwx排列顺序，有下列对应关系：
````
r = 4
w = 2
x = 1
- = 0
另一种方式：
7->二进制为111 及 r,w,x三种权限都有

````
###cd               切换目录

###touch          创建空文件
>touch [-acfm][-d<日期时间>][-r<参考文件或目录>] [-t<日期时间>][--help][--version][文件或目录…]
````
-a   或--time=atime或--time=access或--time=use 　只更改存取时间。

-c   或--no-create 　不建立任何文档。

-d 　使用指定的日期时间，而非现在的时间。

-f 　此参数将忽略不予处理，仅负责解决BSD版本touch指令的兼容性问题。

-m   或--time=mtime或--time=modify 　只更改变动时间。

-r 　把指定文档或目录的日期时间，统统设成和参考文档或目录的日期时间相同。

-t 　使用指定的日期时间，而非现在的时间。
````

###echo            创建带有内容的文件。
>echo [选项] [输出内容]

选项：

    -e：支持反斜线控制的字符转换（具体参见表 1）
    -n：取消输出后行末的换行符号（内容输出后不换行）
    -E 禁用解释反斜杠的转义功能(默认)
````
#!/bin/bash  
echo "Raspberry" > test.txt  
#>直接覆盖文件原有内容
echo "Intel Galileo" >> test.txt  
#>在原本文件后继续换行追加内容
````

###cat              查看文件内容
>cat [选项] [文件]
>将文件或标准输入组合输出到标准输出
 如果没有指定文件，或文件为’-’，则从标准输入读取
 
>>注意：当文件较大时，文本在屏幕上迅速闪过（滚屏），用户往往看不清显示的内容。因此，一般用more等命令分屏显示。为了控制滚屏，可以按Ctrl+S停止滚屏；Ctrl+QQ回复滚屏；Ctrl+C终止该命令，并回到Shell提示符状态。

选项：
````
-n 或 --number：              由 1 开始对所有输出的行数编号。
-b 或 --number-nonblank：     和 -n 相似，只不过对于空白行不编号。
-s 或 --squeeze-blank：       当遇到有连续两行以上的空白行，就代换为一行的空白行。
-v 或 --show-nonprinting：    使用 ^ 和 M- 符号，除了 LFD 和 TAB 之外。
-E 或 --show-ends :           在每行结束处显示 $。
-T 或 --show-tabs:            将 TAB 字符显示为 ^I。
-A, --show-all：              等价于 -vET。
-e：                          等价于"-vE"选项；
-t：                          等价于"-vT"选项；
````
>把 textfile1 的文档内容加上行号后输入 textfile2 这个文档里：
````
cat -n textfile1 > textfile2
````
>把 textfile1 和 textfile2 的文档内容加上行号（空白行不加）之后将内容附加到 textfile3 文档里：
````
cat -b textfile1 textfile2 >> textfile3
````
>清空 /etc/test.txt 文档内容：
````
cat /dev/null > /etc/test.txt
````
>cat 也可以用来制作镜像文件。例如要制作软盘的镜像文件，将软盘放好后输入：
````
cat /dev/fd0 > OUTFILE
````
>相反的，如果想把 image file 写到软盘，输入：
````
cat IMG_FILE > /dev/fd0
````
>注：
>>1. OUTFILE 指输出的镜像文件名。
>>2. IMG_FILE 指镜像文件。
>>3. 若从镜像文件写回 device 时，device 容量需与相当。
>>4. 通常用制作开机磁片。

###cp                拷贝
>cp [options] source dest   或    cp [options] source... directory
````
-a：     此选项通常在复制目录时使用，它保留链接、文件属性，并复制目录下的所有内容。其作用等于dpR参数组合。
-d：     复制时保留链接。这里所说的链接相当于Windows系统中的快捷方式。
-f：     覆盖已经存在的目标文件而不给出提示。
-i：     与-f选项相反，在覆盖目标文件之前给出提示，要求用户确认是否覆盖，回答"y"时目标文件将被覆盖。
-p：     除复制文件的内容外，还把修改时间和访问权限也复制到新文件中。
-r：     若给出的源文件是一个目录文件，此时将复制该目录下所有的子目录和文件。
-l：     不复制文件，只是生成链接文件。
````
>使用指令"cp"将当前目录"test/"下的所有文件复制到新目录"newtest"下，输入如下命令：
````
cp –r test/ newtest 
````      
>>注意：用户使用该指令复制目录时，必须使用参数"-r"或者"-R"。

###mv               移动或重命名
>mv [options] source dest    或    mv [options] source... directory
````
-i:     若指定目录已有同名文件，则先询问是否覆盖旧文件;
-f:     在mv操作要覆盖某已有的目标文件时不给任何指示;
````
>mv参数设置与运行结果

<escape>
<table>
<tr>
    <th>命令格式</th>
    <th>运行结果</th>
</tr>
<tr>
    <td>mv 文件名 文件名</td>
    <td>将源文件名改为目标文件名</td>
</tr>
<tr>
    <td>mv 文件名 目录名</td>
    <td>将文件移动到目标目录</td>
</tr>
<tr>
    <td rowspan='2'>mv 目录名 目录名	</td>
    <td>目标目录已存在，将源目录移动到目标目录</td>
</tr>
<tr>
    <td></td>
    <td>目标目录不存在则改名</td>
</tr>
<tr>
    <td>mv 目录名 文件名	</td>
    <td>出错</td>
</tr>
</table>
</escape>


###rm               删除文件
>rm [-dfirv][--help][--version][文件或目录...]

>执行rm指令可删除文件或目录，如欲删除目录必须加上参数”-r”，否则预设仅会删除文件。

     -d或–directory       直接把欲删除的目录的硬连接数据删成0，删除该目录。(目录下为空才可以删除) 
     -f或–force           强制删除文件或目录。 
     -i或–interactive     删除既有文件或目录之前先询问用户。 
     -r或-R或–recursive   递归处理，将指定目录下的所有文件及子目录一并处理。 
     -v或–verbose         显示指令执行过程。
     
>eg:命令当前在Study文件夹级目录。删除Study文件下的test文件夹下的test文件夹
````
QideMacBook-Pro:Study qiwang$ rm -rf /test/test
````

###find              在文件系统中搜索某文件
>find   path   -option   [   -print ]   [ -exec   -ok   command ]   {} \;

>find 根据下列规则判断 path 和 expression，在命令列上第一个 - ( ) , ! 之前的部份为 path，之后的是 expression。如果 path 是空字串则使用目前路径，如果 expression 是空字串则使用 -print 为预设 expression。

>expression 中可使用的选项有二三十个之多，在此只介绍最常用的部份。
````
-mount, -xdev :             只检查和指定目录在同一个文件系统下的文件，避免列出其它文件系统中的文件
-amin n :                   在过去 n 分钟内被读取过
-anewer file :              比文件 file 更晚被读取过的文件
-atime n :                  在过去n天内被读取过的文件
-cmin n :                   在过去 n 分钟内被修改过
-cnewer file :              比文件 file 更新的文件
-ctime n :                  在过去n天内被修改过的文件
-empty :                    空的文件-gid n or -group name : gid 是 n 或是 group 名称是 name
-ipath p, -path p :         路径名称符合 p 的文件，ipath 会忽略大小写
-name name, -iname name :   文件名称符合 name 的文件。iname 会忽略大小写
-size n :                   文件大小 是 n 单位，b 代表 512 位元组的区块，c 表示字元数，k 表示 kilo bytes，w 是二个位元组。
-type c :                   文件类型是 c 的文件。

d: 目录
c: 字型装置文件
b: 区块装置文件
p: 具名贮列
f: 一般文件
l: 符号连结
s: socket
-pid n : process id 是 n 的文件
你可以使用 ( ) 将运算式分隔，并使用下列运算。
exp1 -and exp2
! expr
-not expr
exp1 -or exp2
exp1, exp2
````
实例：
>将目前目录及其子目录下所有延伸档名是 c 的文件列出来。
````
# find . -name "*.c"
````
>将目前目录其其下子目录中所有一般文件列出
````
# find . -type f
````
>将目前目录及其子目录下所有最近 20 天内更新过的文件列出
````
# find . -ctime -20
````
>查找/var/log目录中更改时间在7日以前的普通文件，并在删除之前询问它们：
````
# find /var/log -type f -mtime +7 -ok rm {} \;
````
>查找前目录中文件属主具有读、写权限，并且文件所属组的用户和其他用户具有读权限的文件：
````
# find . -type f -perm 644 -exec ls -l {} \;
````
>为了查找系统中所有文件长度为0的普通文件，并列出它们的完整路径：
````
# find / -type f -size 0 -exec ls -l {} \;
````

###wc                统计文本中行数、字数、字符数
>wc [-clw][--help][--version][文件...]

参数：
````
-c或--bytes或--chars          只显示Bytes数。
-l或--lines                   只显示行数。
-w或--words                   只显示字数。
--help                        在线帮助。
--version                     显示版本信息。
````
>在默认的情况下，wc将计算指定文件的行数、字数，以及字节数。使用的命令为：
````
$ wc testfile           # testfile文件的统计信息  
 3 92 598 testfile       # testfile文件的行数为3、单词数92、字节数598 
````
>其中，3 个数字分别表示testfile文件的行数、单词数，以及该文件的字节数。
>如果想同时统计多个文件的信息，例如同时统计testfile、testfile_1、testfile_2，可使用如下命令：
```` 
 wc testfile testfile_1 testfile_2   #统计三个文件的信息 
````
>输出结果如下：
````
 $ wc testfile testfile_1 testfile_2  #统计三个文件的信息  
 3 92 598 testfile                    #第一个文件行数为3、单词数92、字节数598  
 9 18 78 testfile_1                   #第二个文件的行数为9、单词数18、字节数78  
 3 6 32 testfile_2                    #第三个文件的行数为3、单词数6、字节数32  
 15 116 708 总用量                    #三个文件总共的行数为15、单词数116、字节数708 
````

###grep             在文本文件中查找某个字符串
>grep [-abcEFGhHilLnqrsvVwxy][-A<显示列数>][-B<显示列数>][-C<显示列数>][-d<进行动作>][-e<范本样式>][-f<范本文件>][--help][范本样式][文件或目录...]

>参数
````
-E ：开启扩展（Extend）的正则表达式。

　　-i ：忽略大小写（ignore case）。

　　-v ：反过来（invert），只打印没有匹配的，而匹配的反而不打印。

　　-n ：显示行号

　　-w ：被匹配的文本只能是单词，而不能是单词中的某一部分，如文本中有liker，而我搜寻的只是like，就可以使用-w选项来避免匹配liker

　　-c ：显示总共有多少行被匹配到了，而不是显示被匹配到的内容，注意如果同时使用-cv选项是显示有多少行没有被匹配到。

　　-o ：只显示被模式匹配到的字符串。

　　--color :将匹配到的内容以颜色高亮显示。

　　-A  n：显示匹配到的字符串所在的行及其后n行，after

　　-B  n：显示匹配到的字符串所在的行及其前n行，before

　　-C  n：显示匹配到的字符串所在的行及其前后各n行，context````
实例：
>1、在当前目录中，查找后缀有 file 字样的文件中包含 test 字符串的文件，并打印出该字符串的行。此时，可以使用如下命令：
````
$ grep test test* #查找前缀有“test”的文件包含“test”字符串的文件  
testfile1:This a Linux testfile! #列出testfile1 文件中包含test字符的行  
testfile_2:This is a linux testfile! #列出testfile_2 文件中包含test字符的行  
testfile_2:Linux test #列出testfile_2 文件中包含test字符的行 
````
>以递归的方式查找符合条件的文件。例如，查找指定目录/etc/acpi 及其子目录（如果存在子目录的话）下所有文件中包含字符串"update"的文件，并打印出该字符串所在行的内容，使用的命令为：
````
$ grep -r update /etc/acpi #以递归的方式查找“etc/acpi”  
#下包含“update”的文件  
/etc/acpi/ac.d/85-anacron.sh:# (Things like the slocate updatedb cause a lot of IO.)  
Rather than  
/etc/acpi/resume.d/85-anacron.sh:# (Things like the slocate updatedb cause a lot of  
IO.) Rather than  
/etc/acpi/events/thinkpad-cmos:action=/usr/sbin/thinkpad-keys--update 
````
>3、反向查找。前面各个例子是查找并打印出符合条件的行，通过"-v"参数可以打印出不符合条件行的内容。
 查找文件名中包含 test 的文件中不包含test 的行，此时，使用的命令为：
 ````
 $ grep-v test* #查找文件名中包含test 的文件中不包含test 的行  
 testfile1:helLinux!  
 testfile1:Linis a free Unix-type operating system.  
 testfile1:Lin  
 testfile_1:HELLO LINUX!  
 testfile_1:LINUX IS A FREE UNIX-TYPE OPTERATING SYSTEM.  
 testfile_1:THIS IS A LINUX TESTFILE!  
 testfile_2:HELLO LINUX!  
 testfile_2:Linux is a free unix-type opterating system. 
 ````

###rmdir           删除空目录
>rmdir [-p] dirName

>参数：
````
-p 是当子目录被删除后使它也成为空目录的话，则顺便一并删除。
````
>实例

>>将工作目录下，名为 AAA 的子目录删除 :
````
rmdir AAA
````
>>在工作目录下的 BBB 目录中，删除名为 Test 的子目录。若 Test 删除后，BBB 目录成为空目录，则 BBB 亦予删除。
````
rmdir -p BBB/Test
````

###tree             树形结构显示目录，需要安装tree包
>tree [-aACdDfFgilnNpqstux][-I <范本样式>][-P <范本样式>][目录...]

>参数说明：
* -a 显示所有文件和目录。
* -A 使用ASNI绘图字符显示树状图而非以ASCII字符组合。
* -C 在文件和目录清单加上色彩，便于区分各种类型。
* -d 显示目录名称而非内容。
* -D 列出文件或目录的更改时间。
* -f 在每个文件或目录之前，显示完整的相对路径名称。
* -F 在执行文件，目录，Socket，符号连接，管道名称名称，各自加上"*","/","=","@","|"号。
* -g 列出文件或目录的所属群组名称，没有对应的名称时，则显示群组识别码。
* -i 不以阶梯状列出文件或目录名称。
* -I<范本样式> 不显示符合范本样式的文件或目录名称。
* -l 如遇到性质为符号连接的目录，直接列出该连接所指向的原始目录。
* -n 不在文件和目录清单加上色彩。
* -N 直接列出文件和目录名称，包括控制字符。
* -p 列出权限标示。
* -P<范本样式> 只显示符合范本样式的文件或目录名称。
* -q 用"?"号取代控制字符，列出文件和目录名称。
* -s 列出文件或目录大小。
* -t 用文件和目录的更改时间排序。
* -u 列出文件或目录的拥有者名称，没有对应的名称时，则显示用户识别码。
* -x 将范围局限在现行的文件系统中，若指定目录下的某些子目录，其存放于另一个文件系统上，则将该子目录予以排除在寻找范围外。

>实例
* 以树状图列出当前目录结构。可直接使用如下命令：
````
$ tree
.
├── file1
├── file2
├── file3
├── test3.zip
└── test_notnull.zip
````

###pwd              显示当前目录
>pwd [--help][--version]

>参数
````
--help 在线帮助。
--version 显示版本信息。
````
>实例：
````
# pwd
/root/test           #输出结果
````
###ln                  创建链接文件
> ln [参数][源文件或目录][目标文件或目录]

>>Linux ln命令是一个非常重要命令，它的功能是为某一个文件在另外一个位置建立一个同步的链接。
  当我们需要在不同的目录，用到相同的文件时，我们不需要在每一个需要的目录下都放一个必须相同的文件，我们只要在某个固定的目录，放上该文件，然后在 其它的目录下用ln命令链接（link）它就可以，不必重复的占用磁盘空间。

>命令功能 : 
>>Linux文件系统中，有所谓的链接(link)，我们可以将其视为档案的别名，而链接又可分为两种 : 硬链接(hard link)与软链接(symbolic link)，硬链接的意思是一个档案可以有多个名称，而软链接的方式则是产生一个特殊的档案，该档案的内容是指向另一个档案的位置。硬链接是存在同一个文件系统中，而软链接却可以跨越不同的文件系统。
不论是硬链接或软链接都不会将原本的档案复制一份，只会占用非常少量的磁碟空间。
* 软链接：
    * 软链接，以路径的形式存在。类似于Windows操作系统中的快捷方式
    * 软链接可以 跨文件系统 ，硬链接不可以
    * 软链接可以对一个不存在的文件名进行链接
    * 软链接可以对目录进行链接
* 硬链接：
    * 硬链接，以文件副本的形式存在。但不占用实际空间。
    * 不允许给目录创建硬链接
    * 硬链接只有在同一个文件系统中才能创建
    
>命令参数
 >>必要参数：
 ````
 -b 删除，覆盖以前建立的链接
 -d 允许超级用户制作目录的硬链接
 -f 强制执行
 -i 交互模式，文件存在则提示用户是否覆盖
 -n 把符号链接视为一般目录
 -s 软链接(符号链接) (不填默认硬链接)
 -v 显示详细的处理过程
 ````
 >> 选择参数：
 ````
 -S "-S<字尾备份字符串> "或 "--suffix=<字尾备份字符串>"
 -V "-V<备份方式>"或"--version-control=<备份方式>"
 --help 显示帮助信息
 --version 显示版本信息
 ````
 
 >实例
 
  * 给文件创建软链接，为log2013.log文件创建软链接link2013，如果log2013.log丢失，link2013将失效：
  ````
  ln -s log2013.log link2013
  ````
  * 给文件创建硬链接，为log2013.log创建硬链接ln2013，log2013.log与ln2013的各项属性相同
  ````
  ln log2013.log ln2013
  ````
 
###more、less  分页显示文本文件内容
>详情参照
* [more_外部link](https://www.runoob.com/linux/linux-comm-more.html)
* [less_外部link](https://www.runoob.com/linux/linux-comm-less.html)

###head、tail    显示文件头、尾内容
>head [选项] [文件..]

>参数：
````
-c, --bytes=[-]K 　　         k,显示文档开始的前k个字节，-k,不显示文档结尾的最后 k 个字节
-n, --lines=[-]K 　　         k,显示文档开始的前k行，-k,不显示文档结尾的最后 k 行
-q, --quiet, --silent        不显示包含给定文件名的文件头
-v, --verbose	　　  	     总是显示包含给定文件名的文件头
--help	　　　　　             显示此帮助信息并退出
--version	　　 　　         显示版本信息并退出
````
* 显示前面5行内容
````
$ head -5 a.txt 
01
02
03
04
05
$ head -n 5 a.txt #带 -n,正数表示前几行，负数表示出去最后几行
01
02
03
04
05
````
* 显示除了  a.txt  最后 10 行的内容
````
$ head -n -10 a.txt 
01
02
````
>tail [参数] [文件] 

>详细参照：
* [tail_link](https://www.runoob.com/linux/linux-comm-tail.html)

###ctrl+alt+F1  命令行全屏模式
>ctrl+Alt+f1~f6通过多用户登录都是终端登录

>Ctrl+alt+f7图形化打开

##系统管理指令
###stat              显示指定文件的详细信息，比ls更详细
>stat [文件或目录]

>实例：
查看 testfile 文件的inode内容内容，可以用以下命令：
````
 # stat testfile
 执行以上命令输出结果：
 # stat testfile                #输入命令
   File: `testfile'
   Size: 102             Blocks: 8          IO Block: 4096   regular file
 Device: 807h/2055d      Inode: 1265161     Links: 1
 Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)
 Access: 2014-08-13 14:07:20.000000000 +0800
 Modify: 2014-08-13 14:07:07.000000000 +0800
 Change: 2014-08-13 14:07:07.000000000 +0800
````

###who               显示在线登陆用户
>who - [husfV] [user]

>参数说明
````
-H 或 --heading：显示各栏位的标题信息列；
-i 或 -u 或 --idle：显示闲置时间，若该用户在前一分钟之内有进行任何动作，将标示成"."号，如果该用户已超过24小时没有任何动作，则标示出"old"字符串；
-m：此参数的效果和指定"am i"字符串相同；
-q 或--count：只显示登入系统的帐号名称和总人数；
-s：此参数将忽略不予处理，仅负责解决who指令其他版本的兼容性问题；
-w 或-T或--mesg或--message或--writable：显示用户的信息状态栏；
--help：在线帮助；
--version：显示版本信息
````

>实例：
>显示当前登录系统的用户
````
# who  //显示当前登录系统的用户
root   tty7     2014-05-13 12:12 (:0)
root   pts/0    2014-05-14 17:09 (:0.0)
root   pts/1    2014-05-14 18:51 (192.168.1.17)
root   pts/2    2014-05-14 19:48 (192.168.1.17)
````

>显示标题栏
````
# who -H
NAME   LINE     TIME       COMMENT
root   tty7     2014-05-13 12:12 (:0)
root   pts/0    2014-05-14 17:09 (:0.0)
root   pts/1    2014-05-14 18:51 (192.168.1.17)
root   pts/2    2014-05-14 19:48 (192.168.1.17)
````

>显示用户登录来源
````
# who -l -H
NAME   LINE     TIME       IDLE     PID COMMENT
LOGIN  tty4     2014-05-13 12:11        852 id=4
LOGIN  tty5     2014-05-13 12:11        855 id=5
LOGIN  tty2     2014-05-13 12:11        862 id=2
LOGIN  tty3     2014-05-13 12:11        864 id=3
LOGIN  tty6     2014-05-13 12:11        867 id=6
LOGIN  tty1     2014-05-13 12:11       1021 id=1
````

>显示终端属性
````
# who -T -H
NAME    LINE     TIME       COMMENT
root   + tty7     2014-05-13 12:12 (:0)
root   + pts/0    2014-05-14 17:09 (:0.0)
root   - pts/1    2014-05-14 18:51 (192.168.1.17)
root   - pts/2    2014-05-14 19:48 (192.168.1.17)
````

>只显示当前用户
````
# who -m -H
NAME   LINE     TIME       COMMENT
root   pts/1    2014-05-14 18:51 (192.168.1.17)
````

###whoami          显示当前操作用户
>whoami [--help][--version]

>实例
显示用户名
````
$:test qiwang$ whoami
 qiwang
````

###hostname      显示主机名

###uname           显示系统信息

###top                动态显示当前耗费资源最多进程信息

###ps                  显示瞬间进程状态 ps -aux
>ps [options] [--help]

>参数说明
````
-A 列出所有的行程
-w 显示加宽可以显示较多的资讯
-au 显示较详细的资讯
-aux 显示所有包含其他使用者的行程
au(x) 输出格式 :
USER PID %CPU %MEM VSZ RSS TTY STAT START TIME COMMAND
USER: 行程拥有者
PID: pid
%CPU: 占用的 CPU 使用率
%MEM: 占用的记忆体使用率
VSZ: 占用的虚拟记忆体大小
RSS: 占用的记忆体大小
TTY: 终端的次要装置号码 (minor device number of tty)
STAT: 该行程的状态:
D: 无法中断的休眠状态 (通常 IO 的进程)
R: 正在执行中
S: 静止状态
T: 暂停执行
Z: 不存在但暂时无法消除
W: 没有足够的记忆体分页可分配
<: 高优先序的行程
N: 低优先序的行程
L: 有记忆体分页分配并锁在记忆体内 (实时系统或捱A I/O)
START: 行程开始时间
TIME: 执行的时间
COMMAND:所执行的指令
````
>实例参照[ps_link](https://www.runoob.com/linux/linux-comm-ps.html)
###du                  查看目录大小 du -h /home带有单位显示目录信息
>实例：

>>只显示当前目录下面的子目录的目录大小和当前目录的总的大小，最下面的1288为当前目录的总大小
显示指定文件所占空间
````
# du log2012.log 
300     log2012.log
````
>>方便阅读的格式显示test目录所占空间情况：
````
# du -h test
608K    test/test6
308K    test/test4
4.0K    test/scf/lib
4.0K    test/scf/service/deploy/product
````

###df                  查看磁盘大小 df -h 带有单位显示磁盘信息
>实例
>>显示文件系统的磁盘使用情况统计：
````
# df 
Filesystem     1K-blocks    Used     Available Use% Mounted on 
/dev/sda6       29640780 4320704     23814388  16%     / 
udev             1536756       4     1536752    1%     /dev 
tmpfs             617620     888     616732     1%     /run 
none                5120       0     5120       0%     /run/lock 
none             1544044     156     1543888    1%     /run/shm 
````
>>第一列指定文件系统的名称，第二列指定一个特定的文件系统1K-块1K是1024字节为单位的总内存。用和可用列正在使用中，分别指定的内存量。
  使用列指定使用的内存的百分比，而最后一栏"安装在"指定的文件系统的挂载点。
  df也可以显示磁盘使用的文件系统信息：
````
# df test 
Filesystem     1K-blocks    Used      Available Use% Mounted on 
/dev/sda6       29640780    4320600   23814492  16%       / 
````
>>用一个-i选项的df命令的输出显示inode信息而非块使用量。
````
df -i 
Filesystem      Inodes    IUsed    IFree     IUse% Mounted on 
/dev/sda6      1884160    261964   1622196   14%        / 
udev           212748     560      212188    1%         /dev 
tmpfs          216392     477      215915    1%         /run 
none           216392     3        216389    1%         /run/lock 
none           216392     8        216384    1%         /run/shm 
````
###ifconfig          查看网络情况
>实例
>>显示网络设备信息
````
# ifconfig 
lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
	options=1203<RXCSUM,TXCSUM,TXSTATUS,SW_TIMESTAMP>
	inet 127.0.0.1 netmask 0xff000000 
	inet6 ::1 prefixlen 128 
	inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1 
	nd6 options=201<PERFORMNUD,DAD>
gif0: flags=8010<POINTOPOINT,MULTICAST> mtu 1280
stf0: flags=0<> mtu 1280
XHC20: flags=0<> mtu 0
XHC1: flags=0<> mtu 0
XHC0: flags=0<> mtu 0
VHC128: flags=0<> mtu 0
````
>>启动关闭指定网卡
````
# ifconfig eth0 down
# ifconfig eth0 up
````
>>为网卡配置和删除IPv6地址
````
  # ifconfig eth0 add 33ffe:3240:800:1005::2/ 64 //为网卡诶之IPv6地址
  
  # ifconfig eth0 del 33ffe:3240:800:1005::2/ 64 //为网卡删除IPv6地址
````
>>用ifconfig修改MAC地址
````
# ifconfig eth0 down //关闭网卡
# ifconfig eth0 hw ether 00:AA:BB:CC:DD:EE //修改MAC地址
# ifconfig eth0 up //启动网卡
# ifconfig eth1 hw ether 00:1D:1C:1D:1E //关闭网卡并修改MAC地址 
# ifconfig eth1 up //启动网卡
````
>>配置IP地址
````
  # ifconfig eth0 192.168.1.56 
  //给eth0网卡配置IP地址
  # ifconfig eth0 192.168.1.56 netmask 255.255.255.0 
  // 给eth0网卡配置IP地址,并加上子掩码
  # ifconfig eth0 192.168.1.56 netmask 255.255.255.0 broadcast 192.168.1.255
  // 给eth0网卡配置IP地址,加上子掩码,加上个广播地址
````
>>启用和关闭ARP协议
````
# ifconfig eth0 arp  //开启
# ifconfig eth0 -arp  //关闭
````
>>设置最大传输单元
````
# ifconfig eth0 mtu 1500 
//设置能通过的最大数据包大小为 1500 bytes
````
###ping                测试网络连通
>语法
>ping [-dfnqrRv][-c<完成次数>][-i<间隔秒数>][-I<网络界面>][-l<前置载入>][-p<范本样式>][-s<数据包大小>][-t<存活数值>][主机名称或IP地址]

>参数说明：
````
-d 使用Socket的SO_DEBUG功能。
-c<完成次数> 设置完成要求回应的次数。
-f 极限检测。
-i<间隔秒数> 指定收发信息的间隔时间。
-I<网络界面> 使用指定的网络接口送出数据包。
-l<前置载入> 设置在送出要求信息之前，先行发出的数据包。
-n 只输出数值。
-p<范本样式> 设置填满数据包的范本样式。
-q 不显示指令执行过程，开头和结尾的相关信息除外。
-r 忽略普通的Routing Table，直接将数据包送到远端主机上。
-R 记录路由过程。
-s<数据包大小> 设置数据包的大小。
-t<存活数值> 设置存活数值TTL的大小。
-v 详细显示指令的执行过程。
````
实例：
>检测是否与主机连通

````
# ping www.w3cschool.cc //ping主机
//注意：需要手动终止Ctrl+C
PING aries.m.alikunlun.com (114.80.174.110) 56(84) bytes of data.
64 bytes from 114.80.174.110: icmp_seq=1 ttl=64 time=0.025 ms
64 bytes from 114.80.174.110: icmp_seq=2 ttl=64 time=0.036 ms
64 bytes from 114.80.174.110: icmp_seq=3 ttl=64 time=0.034 ms
64 bytes from 114.80.174.110: icmp_seq=4 ttl=64 time=0.034 ms
64 bytes from 114.80.174.110: icmp_seq=5 ttl=64 time=0.028 ms
64 bytes from 114.80.174.110: icmp_seq=6 ttl=64 time=0.028 ms
64 bytes from 114.80.174.110: icmp_seq=7 ttl=64 time=0.034 ms
64 bytes from 114.80.174.110: icmp_seq=8 ttl=64 time=0.034 ms
64 bytes from 114.80.174.110: icmp_seq=9 ttl=64 time=0.036 ms
64 bytes from 114.80.174.110: icmp_seq=10 ttl=64 time=0.041 ms

--- aries.m.alikunlun.com ping statistics ---
10 packets transmitted, 30 received, 0% packet loss, time 29246ms
rtt min/avg/max/mdev = 0.021/0.035/0.078/0.011 ms
````
>多参数使用
````
# ping -i 3 -s 1024 -t 255 g.cn //ping主机
//-i 3 发送周期为 3秒 -s 设置发送包的大小 -t 设置TTL值为 255
PING g.cn (203.208.37.104) 1024(1052) bytes of data.
1032 bytes from bg-in-f104.1e100.net (203.208.37.104): icmp_seq=0 ttl=243 time=62.5 ms
1032 bytes from bg-in-f104.1e100.net (203.208.37.104): icmp_seq=1 ttl=243 time=63.9 ms
1032 bytes from bg-in-f104.1e100.net (203.208.37.104): icmp_seq=2 ttl=243 time=61.9 ms

--- g.cn ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 6001ms
rtt min/avg/max/mdev = 61.959/62.843/63.984/0.894 ms, pipe 2
[root@linux ~]# 
````
###netstat          显示网络状态信息
>语法
netstat [-acCeFghilMnNoprstuvVwx][-A<网络类型>][--ip]
>参数说明：
````
-a或--all 显示所有连线中的Socket。
-A<网络类型>或--<网络类型> 列出该网络类型连线中的相关地址。
-c或--continuous 持续列出网络状态。
-C或--cache 显示路由器配置的快取信息。
-e或--extend 显示网络其他相关信息。
-F或--fib 显示FIB。
-g或--groups 显示多重广播功能群组组员名单。
-h或--help 在线帮助。
-i或--interfaces 显示网络界面信息表单。
-l或--listening 显示监控中的服务器的Socket。
-M或--masquerade 显示伪装的网络连线。
-n或--numeric 直接使用IP地址，而不通过域名服务器。
-N或--netlink或--symbolic 显示网络硬件外围设备的符号连接名称。
-o或--timers 显示计时器。
-p或--programs 显示正在使用Socket的程序识别码和程序名称。
-r或--route 显示Routing Table。
-s或--statistice 显示网络工作信息统计表。
-t或--tcp 显示TCP传输协议的连线状况。
-u或--udp 显示UDP传输协议的连线状况。
-v或--verbose 显示指令执行过程。
-V或--version 显示版本信息。
-w或--raw 显示RAW传输协议的连线状况。
-x或--unix 此参数的效果和指定"-A unix"参数相同。
--ip或--inet 此参数的效果和指定"-A inet"参数相同。
````
>实例
>显示详细的网络状况
````
 # netstat -a
````
>显示当前户籍UDP连接状况
````
 # netstat -nu
````
###man                命令不会用了，找男人  如：man ls
>man手册的使用方法
 
    例如：man ls  后
 
 >>查看时需要翻屏：
 
   * 向后翻一屏：space(空格键)    　　
   * 向前翻一屏：b
   * 向后翻一行：Enter(回车键)    　　 
   * 向前翻一行：k
 
  >>查看时需要查找：
 
   * /关键词      向后查找    n：下一个
   * ?关键词     向前查找    N：前一个
   
  >>退出man：q
 
>标准用户命令

  >>可以使用whatis命令是用于查询一个命令执行什么功能，并将查询结果打印到终端上。
  例如：
  ````
  [root@nfs-server ~]#whatis cd
  
  cd (1p)  　　　　- change the working directory
  
  cd [builtins] (1)    - bash built-in commands, see bash(1)
  
  #从上文的输出结果我们看到cd命令是bash的内建命令，它的功能是改变当前目录，可以在1和1p的章节中查看它的帮助。
  ````

###clear              清屏

###alias               对命令重命名 如：alias showmeit="ps -aux" ，另外解除使用unaliax showmeit
>语法
 
 * alias[别名]=[指令名称]
 
>参数说明：若不加任何参数，则列出目前所有的别名设置。

###kill                 杀死进程，可以先用ps 或 top命令查看进程的id，然后再用kill命令杀死进程。
>语法

 * kill [-s <信息名称或编号>][程序]　或　kill [-l <信息编号>]
 
>参数说明

* -l <信息编号> 　若不加<信息编号>选项，则-l参数会列出全部的信息名称。
* -s <信息名称或编号> 　指定要送出的信息。
* [程序] 　[程序]可以是程序的PID或是PGID，也可以是工作编号。

>实例：

* 杀死进程
````
  # kill 12345
````

* 强制杀死进程
````
  # kill -KILL 123456
````
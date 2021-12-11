# 文件介绍

## requirements.txt：

相关依赖在里面。python版本为3.9。

## main.py：

创建数据库模式

## write.py：

从excel表格中读取数据然后加入到数据库中。

使用方法：

**1.修改write_file_index:**

不同表格对应不同index：

![image-20211211124748464](C:\Users\hasee\AppData\Roaming\Typora\typora-user-images\image-20211211124748464.png)

例如family_fygx_cases对应家庭关系中抚养关系表格（fygx），index为2。

**2.修改这一句代码：**

![image-20211211125157824](C:\Users\hasee\AppData\Roaming\Typora\typora-user-images\image-20211211125157824.png)

根据要存的表格修改路径：![image-20211211125351818](C:\Users\hasee\AppData\Roaming\Typora\typora-user-images\image-20211211125351818.png)

sheet_name:表示excel中第几个sheet，从零开始

usecols:使用excel表格中的哪几列，因为只需要案子名字，裁判理由，结果。所以就选了那三列

skiprows：跳过哪几行。因为第一第二行为空，所以我跳过。

==**现存问题：**==

（1）从excel中读取的数据有/r这种符号。

![image-20211211125737431](C:\Users\hasee\AppData\Roaming\Typora\typora-user-images\image-20211211125737431.png)



（2）还没有把裁判理由中的法律法规单独提取出来。

## search.py：

根据用户输入，搜索内容。

使用方法：

1.修改input。把input的内容改为用户输入即可。

![image-20211211130153593](C:\Users\hasee\AppData\Roaming\Typora\typora-user-images\image-20211211130153593.png)

2.修改file_index。指明是在类别的表格中找。

![image-20211211124748464](C:\Users\hasee\AppData\Roaming\Typora\typora-user-images\image-20211211124748464.png)
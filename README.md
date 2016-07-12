## 用途 ##

这个小工具可以帮助HR批量地按照给定模板发送工资单给多个员工.

<!--### 环境配置 ###-->

<!--####Mac OSX####-->

<!--1. 安装pip-->
<!--`brew install pip`-->


<!--####Windows####-->

<!--1. 安装python-->


### 邮箱设置 ###

修改email.txt

````
[sender]               //发送的邮箱
xiaoke.jia@hobot.cc

[username]             //登陆邮箱系统的用户名(不一定是邮箱号)
xiaoke.jia

[password]             //登陆邮箱系统的密码
123456

[serveraddr]           //邮箱系统的smtp服务器地址
mail.hobot.cc

[serverport]           //邮箱系统smtp服务器的端口号
123

[debug]                //是否打印调试信息
false
````

### 工资单 ###

目前支持.csv格式. Excel可以直接把.xlsx另存为.csv
注意把第一行必须是表的列名. test.csv中给出了一个示例.

### 邮件模板 ###

* 一个正确邮件模板包括四个部分:FROM, TO, SUBJECT和CONTENT
* 每个部分需要填充的内容模板写在下一行. 
* 部分与部分之间用一个*空行*分割(不要加空格). 
* 花括号{}代表这个位置会填充工资文件中的*对应列名*的值. 

比如示例模板test_template.txt中间的四部分为. 

````````
FROM
人力资源 <{from}>

TO
{邮箱}

SUBJECT
{月份}月工资单

CONTENT
这里开始是正文, blablabla

你本月工资{wage}元, 税{tax}元, 税务的比例为{ratio}...

祝好,

人力资源
H(ighness) R(oyal)

````````

## 用法 ##

### Mac OS ###

1. 双击EasyNotify.app运行
2. 按照提示输入工资文件(.csv)和邮件模板文件(e.g. test_template.txt)
3. 选择邮箱配置文件, 直接回车将从默认的邮箱配置文件(email.txt)中加载
4. 随机预览一封邮件, 如果没有问题, 输入y回车开始发送.

### 命令行 ###
`python EasyNotify.py 工资文件 邮件模板`

示例:

1. 给test.csv的每个人,按照模板temp1.txt发送邮件: 
`python EasyNotify.py test.csv temp1.txt` 

2. 给intrn.cvs的每个人,按照模板intern.txt发送, 同时抄送自己 
`python EasyNotify.py intrn.csv intern.txt --ccself`

3. 用另一个邮箱配置文件(new_email.txt)发送邮件, 并抄送自己 
`python EasyNotify.py intrn.csv intern.txt -c -m new_email.txt`

4. 口..口 
`python EasyNotify.py intrn.csv intern.txt -excited`



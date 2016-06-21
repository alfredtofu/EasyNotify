
** 用途 **

这个小工具可以帮助HR批量地按照给定模板发送工资单给多个员工.

*** 邮箱设置 ***

修改email.conf

````
{
"sender" : "jiaxiaoke@hobot.cc",   //发送的邮箱
"username" : "jiaxiaoke",          //登陆邮箱系统的用户名(不一定是邮箱号)
"password" : "1234qwer",           //登陆邮箱系统的密码
"serveraddr" : "smtp.qq.com",      //邮箱系统的smtp服务器地址
"serverport" : "587",              //邮箱系统smtp服务器的端口号
"debug" : false                    //是否打印调试信息
}
````

*** 工资单 ***

目前支持.csv格式. Excel可以直接把.xlsx另存为.csv
注意把第一行必须是表的列名. test.csv中给出了一个示例.

*** 邮件模板 ***

一个正确邮件模板包括四个部分, 每个部分用一个*空行*分割(不要加空格). 花括号{}代表这个位置会填充工资文件中的*对应列名*的值. 比如示例模板WageTemplate01.txt中间的四部分为:

````````
FROM
人力资源 <{from}>

TO
{邮箱}

SUBJECT
{月份}月工资单

CONTENT
这里是正文, blablabla

````````

** 用法 **

python EasyNotify.py 工资文件 邮件模板

示例:

1. 给employee.xls的每个人,按照模板employee.txt发送邮件:

python EasyNotify.py  employee.xml employee.txt

2. 给intrn.xls的每个人,按照模板intern.txt发送, 同时抄送自己

python EasyNotify.py intrn.xls intern.txt -ccself




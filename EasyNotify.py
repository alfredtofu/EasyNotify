#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import math
import csv
import json
import io
import argparse
import random
from lib.utils import *
from lib.EmailSender import *
from lib.WageReader import *
from os import path
def preview():
    pass

def send():
    pass

def main():
    name = os.path.basename(sys.argv[0])
    desc =  u"用法: python {0} 工资文件 模板文件 [-m] [-c] [-e]\n".format(name) + \
            u"--------------------------------------------\n" + \
            u"示例:\n\n".format() + \
            u"1. 给test.csv的每个人,按照模板temp1.txt发送邮件:\n" + \
            u"python {0} test.csv temp1.txt\n\n".format(name) + \
            u"2. 给intrn.cvs的每个人,按照模板intern.txt发送, 同时抄送自己\n" + \
            u"python {0} intrn.csv intern.txt --ccself\n\n".format(name) + \
            u"3. 用另一个邮箱配置文件(new_email.txt)发送邮件, 并抄送自己\n" + \
            u"python {0} intrn.csv intern.txt -c -m new_email.txt\n\n".format(name) + \
            u"4. 口..口\n" + \
            u"python {0} intrn.csv intern.txt -excited\n\n".format(name)

    assert_msg (len(sys.argv) > 1, desc + " ".join(sys.argv))

    parser = argparse.ArgumentParser(
        prog=sys.argv[0],
        formatter_class=argparse.RawTextHelpFormatter,
        description = desc

    )
    parser.add_argument('wage_file' , type=str, help=u'''工资文件位置''')
    parser.add_argument('template_file',  type=str, help=u"模板文件位置")
    parser.add_argument('-c','--ccself', action="store_true", default=False, required = False, help=u"可选: 抄送自己")
    parser.add_argument('-m','--mail', type=str, default='email.txt', help=u"可选: 邮箱配置")
    parser.add_argument('-e', '--excited', action="store_true", default=False, help=u"口..口")
    args= parser.parse_args()

    table_file = args.wage_file
    template_file = args.template_file
    ccself = args.ccself
    excited = args.excited
    emailfile = args.mail

    if excited:
        print_him()

    config = WageNotifierSetting.createFromFile(emailfile)
    reader = WageReader(table_file)
    sender = EmailNotifier(config)
    rows = reader.read_rows()

    if sender.server is None or rows is None:
        return

    tasks = []

    i = 0
    print u"检查工资单和邮件模板..."
    for row in rows:
        i+=1
        try:
            row[u'from'] = config.sender
            task = WageTask.createTaskFromRow(row, template_file, ccself)
            if task is not None:
                tasks.append(task)
        except IOError as e:
            print u"模板文件错误:\n   {0}".format(e.message)
            return
        except Exception as e:
            print u"错误, 检查工资文件第{0}行出现错误:\n\t{1}\n".format(i, e.message)
            return
    print u"检查通过\n"

    if len(tasks) == 0:
        print u"工资单为空...即将退出..."
        return

    print u"发送邮件给{0}名员工, 模板{1}...\n".format(len(tasks), path.basename(template_file))
    print u"========邮件预览========"
    print tasks[random.randint(1, len(tasks)) - 1].__str__()
    print u"========预览结束========\n"

    Y = raw_input(u"若预览无误,输入y开始发送, 输入其他字符退出...\n".encode(sys.stdout.encoding))
    if Y.lower().strip() != u"y":
        print u"即将退出\n"
        return


    i = 0
    for task in tasks:
        i+=1
        print u"{0}: 正在发送邮件给 {1}...".format(i, task.toaddrs)
        sender.send(task)

    print u"发送完毕...\n\n觉得好用的话请给工具的作者涨工资 :) \n"

if __name__ == "__main__":
    main()
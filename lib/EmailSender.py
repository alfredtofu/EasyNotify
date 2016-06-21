#!/usr/bin/python
# -*- coding: utf-8 -*-

import smtplib
import codecs
import json
import re
import StringIO
from os import path
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

from getpass import getpass

class WageTask:
    fromaddr = ""
    toaddrs = []
    ccaddrs = []
    subject = None
    content = None

    row = None

    template_file = ""

    from_template = None
    to_template = None
    subject_template = None
    content_template = ''

    to_col_name = None

    def __str__(self):
        tpl = u"From: {0}\nTo: {1}\nCC: {2}\n\nSubject: {3}\n\n{4}"
        return tpl.format(
            self.fromaddr,
            u", ".join(self.toaddrs),
            u", ".join(self.ccaddrs),
            self.subject,
            self.content
        )


    @staticmethod
    def createTaskFromRow(row, template_file, ccself = False, sendself = False):
        # 要求输入非空
        if not path.exists(template_file):
            raise IOError(u"错误, 模板文件{0}不存在".format(template_file))

        if row is None or template_file is None:
            raise Exception(u'错误,请检查是否输入内容')

        raw_template = ""
        with codecs.open(template_file, 'r', 'utf-8') as fid:
            for line in fid:
                raw_template += line

        cook_template = raw_template.split('\n\n', 3)
        from_template = cook_template[0]
        to_template = cook_template[1]
        subject_template = cook_template[2]
        content_template = cook_template[3]

        assert (from_template.split("\n")[0].lower() == 'from')
        assert (to_template.split('\n')[0].lower() == 'to')
        assert (subject_template.split('\n')[0].lower() == 'subject')
        assert (content_template.split('\n', 1)[0].lower() == 'content')

        # collect all '{col-name}' in template, and check if exists
        # corresponding col in wage file
        col = re.compile("\{([^\}]{1,10})\}")
        cols = col.findall(raw_template)
        for c in cols:
            if c not in row:
                print (u"错误: 邮件模板中{{{0}}}在工资表中找不到对应的列名".format(c))
                raise Exception(u"错误: 邮件模板中 {{{0}}} 在工资表中找不到对应的列名".format(c))


        task = WageTask()
        task.from_template = from_template.split("\n")[1]
        task.to_template = to_template.split('\n')[1]
        task.subject_template = subject_template.split('\n')[1]
        task.content_template = content_template.split('\n', 1)[1]
        task.to_col_name = re.search("\{([^\}]+)\}", task.to_template).group(1)

        task.fromaddr = task.from_template.format(**row)
        task.toaddrs = [task.to_template.format(**row)]
        task.subject = task.subject_template.format(**row)
        task.content = task.content_template.format(**row)
        task.row = row

        # 如果收件人对应的列是空, 那么就不发送这一行
        if row[task.to_col_name].strip("\n \r") == "":
            return None

        # 检查输入邮箱格式
        prog = re.compile('[^@]+@([^@\.]+\.)+')
        ret = prog.match(task.fromaddr)
        if ret is None:
            logging.error(u'错误,发件人格式不正确')
            raise Exception(u'错误,发件人格式不正确, {0}'.format(task.fromaddr))

        # 检查收件人格式是否正确
        for to_addr in task.toaddrs:
            ret = prog.match(to_addr)
            if ret is None:
                raise Exception(u'错误, 收件人格式不正确 {0}'.format(to_addr) )

        # 是否抄送自己
        if ccself and task.fromaddr not in task.ccaddrs:
            task.ccaddrs.append(task.fromaddr)
        if sendself and task.fromaddr not in task.toaddrs:
            task.toaddrs.append(task.fromaddr)

        return task

class WageNotifierSetting:
    username = ""
    password = ""
    serveraddr = ""
    sender = ""
    debug = None
    @staticmethod
    def createFromJSON(jsonobj):
        setting = WageNotifierSetting()
        setting.username = jsonobj['username']
        setting.password = jsonobj['password']
        setting.serveraddr = jsonobj['serveraddr']
        setting.sender = jsonobj['sender']
        setting.debug = jsonobj['debug']
        return setting

    @staticmethod
    def createFromFile(filename):
        with codecs.open(filename, 'r', 'utf-8') as fid:
            jsonobj = json.load(fid, 'utf-8')
            return WageNotifierSetting.createFromJSON(jsonobj)

class EmailNotifier:

    config = None
    server = None

    def __init__(self, config):
        self.config = config
        # self.server = smtplib.SMTP_SSL(config.serveraddr)
        # self.server.set_debuglevel(1)  # 开启调试，会打印调试信息
        print(u"验证邮箱账户密码...")
        try:
            self.server = smtplib.SMTP(config.serveraddr, 587)
            self.server.set_debuglevel(config.debug)
            self.server.ehlo()
            self.server.starttls()
            self.server.login(config.username, config.password)
            print u"验证通过\n"
        except smtplib.SMTPAuthenticationError as e:
            print(u"验证失败: {0}\n".format(e.smtp_error))
            self.server = None
        except Exception as e:
            print(u"验证失败, 原因未知. 错误信息为: {0}".format(e))
            self.server = None

    def send_batch(self, tasks):
        for task in tasks:
            self.send(task)

    def send(self, task):

        def _format_addr(s):
            name, addr = parseaddr(s)
            return formataddr((
                Header(name, 'utf-8').encode(),
                addr.encode('utf-8') if isinstance(addr, unicode) else addr)
            )

        msg = MIMEText(task.content, 'plain', 'utf-8')
        msg['From'] = _format_addr(u'%s' % task.fromaddr)
        msg['To'] = _format_addr(u', '.join(task.toaddrs) )
        msg['CC'] = _format_addr(u', '.join(task.ccaddrs) )
        msg['Subject'] = Header(task.subject, 'utf-8').encode()

        # print msg
        self.server.sendmail( task.fromaddr, task.toaddrs, msg.as_string())
        # self.server.quit()

    def close(self):
        self.server.quit()

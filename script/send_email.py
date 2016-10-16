#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import smtplib
from config import Config
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

config_file = file('indexer.cfg')
cfg = Config(config_file)

host = cfg.host
port = cfg.port
sender = cfg.sender
pwd = cfg.pwd

def send_email(sendto_list = [cfg.receiver], subject = '', content = '', files = []):
    for sendto in sendto_list:
        msg = MIMEMultipart()     # 设置正文为符合邮件格式的HTML内容
        msg['subject'] = subject            # 设置邮件标题
        msg['from'] = sender                # 设置发送人
        msg['to'] = sendto # 设置接收人
        msg['content'] = content

        for f in files:
            print 'Now sending ', f
            att = MIMEText(open(f).read(), 'base64', 'utf-8')
            att["Content-Type"] = 'application/octet-stream'
            att.add_header("Content-Disposition", "attachment", filename = os.path.basename(f))
            msg.attach(att)

        s = smtplib.SMTP_SSL(host, port)  # 注意！如果是使用SSL端口，这里就要改为SMTP_SSL
        s.login(sender, pwd)
        s.sendmail(sender, msg['to'], msg.as_string())

if __name__ == '__main__':
    send_email(subject = 'email test', content='this is a test email', files = [])
    print 'over'  # 发送成功就会提示

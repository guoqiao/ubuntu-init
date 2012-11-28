#!/usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib

EMAIL_USER = 'spig@insigma.com.cn'
EMAIL_PSWD = '******'
EMAIL_SMTP = 'smtp.insigma.com.cn'
EMAIL_PORT = 587

def sendmail(receivers, subject, message):
    h = smtplib.SMTP(EMAIL_SMTP, EMAIL_PORT)
    h.login(EMAIL_USER, EMAIL_PSWD)
    x = 'From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n%s\r\n' % (EMAIL_USER, ', '.join(receivers), subject, message)
    h.sendmail(EMAIL_USER, receivers, x)
    h.quit()
    print x


SUBJECT = 'message'

MESSAGE = '''
put your message here
'''

RECEIVERS = ['guoqiao.34c12a3@m.yinxiang.com','guoqiao.a38b6@m.evernote.com','guoqiao@gmail.com']

if __name__ == '__main__':
    sendmail(RECEIVERS, SUBJECT, MESSAGE)

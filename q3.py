# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 16:42:55 2020

@author: lisa_
"""


import smtplib
from email.mime.text import MIMEText

mailto_list=["lisa_xulishan@126.com"]
mail_host="smtp.qq.com"
mail_user="1666097083@qq.com"
mail_pass="ohgeyqxytczzighg"

msg = MIMEText("Hello")
msg["Subject"]="Hi"
msg['From']=mail_user
msg['To']=";".join(mailto_list)

try:
    s=smtplib.SMTP()
    s.connect(mail_host)
    s.login(mail_user,mail_pass)
    s.sendmail(mail_user,mailto_list,msg.as_string())
    s.close()
    print("Succeeded")
    
except Exception as e:
    print(str(e) )
    print("Failed" )
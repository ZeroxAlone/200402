# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 16:22:35 2020

@author: lisa_
"""

import poplib
from email import parser
from email.header import decode_header

server = poplib.POP3_SSL('pop.qq.com')
server.user("1666097083")
server.pass_("ohgeyqxytczzighg")

resp, mails, octets = server.list()
print("共有 %d 封邮件。" % len(mails))

for i in range(len(mails)):
    resp, lines, octets = server.retr(i+1)
    msg_content = b'\r\n'.join(lines).decode("utf-8")
    msg = parser.Parser().parsestr(msg_content)
    emailbase={}
    
    for line in msg.items():
        header=line[0]
        if header in ["From","Subject","Date"]:
            item=decode_header(line[1])[-1]
            code=item[1] if item[1]!=None else "ascii"
            if isinstance(item[1], bytes): value = str(item[0], code)
            else : value = item[0]
            emailbase[header]=value

    print("-----------%d/%d-----------"%(i+1, len(mails)))
    print("发信信箱： "+emailbase["From"])
    print("发信主题： "+emailbase["Subject"])
    print("发信时间： "+emailbase["Date"])

server.quit()
0 import smtplib
1 import time
2 import psutil
3 from email.mime.text import MIMEText
4 from email.header import Header
5 6 
7 def sendmail(receivers=['493333629@qq.com']):
8 
9     # 第三方 SMTP 服务
10     mail_host = "smtp.163.com"  # 设置服务器  不要用QQ邮箱
11     mail_user = "mail@163.com"  # 用户名
12     mail_pass = "password"  # 口令
13     # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
14 
15     # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
16     message = MIMEText('进程已经关闭，请注意！', 'plain', 'utf-8')
17     message['From'] = "{}".format(mail_user)
18     message['To'] = ",".join(receivers)
19 
20     subject = '监控进程'
21     message['Subject'] = Header(subject, 'utf-8')
22 
23     try:
24 
25         smtpObj=smtplib.SMTP_SSL(mail_host, 465)  # 25 为 SMTP 端口号
26         smtpObj.login(mail_user, mail_pass)
27         smtpObj.sendmail(mail_user,receivers,message.as_string())
28 
29         print("邮件发送成功")
30     except smtplib.SMTPException as e:
31         print("Error: 无法发送邮件",e)
32 
33 def monitor(taskname='python',username='gdcy'):
34     while True:
35         pid = psutil.pids()
36         found=False
37         for k, i in enumerate(pid):
38             try:
39                 proc = psutil.Process(i)
40                 if proc.name()==taskname and proc.username()==username:
41                     found=True
42 
43             except psutil.AccessDenied:
44                 print("psutil.AccessDenied")
45         if found:
46             time.sleep(1)
47         else:
48             sendmail(['493333629@qq.com'])
49             break
50
51 
52 monitor(taskname='gedit',username='gdcy')
# 发邮件的库
import smtplib
# 邮件文本
from email.mime.text import MIMEText

# smpt服务器
SMTPServer = "smtp.163.com"
# 发邮件的地址
Sender = "15801788751@163.com"
# 发送者邮箱密码(授权密码)
password = "a123456"

# 设置发送的内容
text = "zhao bi cheng is a good man"
# 转换邮件文本
message = MIMEText(text)

# 主题（标题）
message["Subject"] = "来自帅哥的问候"
# 收件者
message["From"] = Sender

# 创建文件服务器
mailServer = smtplib.SMTP(SMTPServer, 25)
# 登录邮箱
mailServer.login(Sender, password)
# 发送邮件
mailServer.sendmail(Sender, ["15801788751@163.com"], message.as_string())
# 退出邮箱
mailServer.quit()
"""
    503错误 一般是内容不合法 或者邮箱有问题
"""

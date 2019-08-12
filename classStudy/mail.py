import smtplib

fromAddress = "1434756304@qq.com"
toAddress = "1434756304@qq.com"
server = smtplib.SMTP("localhost", 25)
server.sendmail(fromAddress, toAddress, msg="Subject:Hello\n\nthis is the body of the message")

'''from email.mime.text import MIMEText
import smtplib


#构造MIMEText对象时，第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'表示纯文本，
#最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。
#msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

# 输入Email地址和口令
#from_addr = input('From:')
#password = input('Password:')
# 输入收件人地址：
#to_addr = input('to:')
# 输入SMTP服务器地址：
#smtp_server = input('SMTP server:')

#server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
#server.set_debuglevel(1)
#server.login(from_addr, password)
#server.sendmail(from_addr, [to_addr], msg.as_string())
#server.quit()
#用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。SMTP协议就是简单的文本命令和响应。
#login()方法用来登录SMTP服务器，sendmail()方法就是发邮件，由于可以一次发给多个人，
#所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str。
'''




from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

'''编写了一个函数_format_addr()来格式化一个邮件地址。注意不能简单地传入name <addr@example.com>，
因为如果包含中文，需要通过Header对象进行编码。'''
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

#from_addr = input('From: ')
from_addr = 'linnahan2017@163.com'
password = input('Password: ')
#to_addr = input('To: ')
to_addr = '1596695476@qq.com'
#smtp_server = input('SMTP server: ')
smtp_server = 'smtp.163.com'



msg = MIMEMultipart('alternative')
# 发送纯文本
#msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
# 发送HTML邮件
'''msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')'''
msg.attach(MIMEText('hello', 'plain', 'utf-8'))
msg.attach(MIMEText('<html><body><h1>Hello</h1></body></html>', 'html', 'utf-8'))
#发送附件
'''带附件的邮件可以看做包含若干部分的邮件：文本和各个附件本身，
所以，可以构造一个MIMEMultipart对象代表邮件本身，然后往里面加上一个MIMEText作为邮件正文，
再继续往里面加上表示附件的MIMEBase对象即可：'''
# 邮件正文是MIMEText:
#msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
# 嵌入图片
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'))
# 如果有多个图片，给它们依次编号，然后引用不同的cid:x即可。
# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open(r'E:\图片\印章\mkllz0hm.png', 'rb') as f:
    # 设置附件的MIME和文件名，这里是jpg类型:
    mime = MIMEBase('image', 'png', filename='mkllz0hm.png')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='mkllz0hm.pngg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)
    
    
    
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()
    
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
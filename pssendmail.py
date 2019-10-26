"""mail client"""
import smtplib
from email.mime.text import MIMEText


smtp_server_address = 'localhost'  # 'mail.danskebank.com'
message = open('passwd.txt').read()

mesg = MIMEText(message)  # instance for the class MIMEText
mesg['From'] = 'ravi@localhost'
mesg['To'] = 'training@localhost'
mesg['Subject'] = 'a test mail to test content'

smtp = smtplib.SMTP(smtp_server_address)
smtp.ehlo()
smtp.debuglevel=1
# smtp.login('user', 'passwd')
smtp.sendmail('ravi@localhost', 'training@localhost', mesg.as_string())
smtp.close()


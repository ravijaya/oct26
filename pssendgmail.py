import smtplib
from email.mime.text import MIMEText
from getpass import getpass

TO = 'ravi.goglobium@gmail.com'
SUBJECT = 'TEST MAIL'


gmail_sender = TO
gmail_passwd = getpass()

server = smtplib.SMTP('smtp.gmail.com', 587)
# server.ehlo()
server.starttls()
server.login(gmail_sender, gmail_passwd)

message = open('passwd.txt').read()
mesg = MIMEText(message)  # instance for the class MIMEText
mesg['From'] = TO
mesg['To'] = TO
mesg['Subject'] = 'a test mail to test content'

try:
    server.sendmail(gmail_sender, TO, mesg.as_string())
    print ('email sent')
except:
    print ('error sending mail')

server.quit()
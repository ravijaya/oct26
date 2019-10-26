"""spreadsheet as attachment"""

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import mimetypes
from psdb2csv import db_to_xlsx


def send_mail(from_addr, to_addr, sub, message):
    spreadsheet = 'test.xlsx'
    db_to_xlsx(spreadsheet)   # prepare the attachment

    m = MIMEMultipart()       # email content
    m["To"] = to_addr
    m["From"] = from_addr
    m["Subject"] = sub

    ctype, encoding = mimetypes.guess_type(spreadsheet)  # 21-25 classify the attachment
    print(ctype, encoding)
    print()
    maintype, subtype = ctype.split('/', 1)
    print(maintype, subtype)

    m.attach(MIMEText(message))  # email body

    fp = open(spreadsheet, 'rb')        # 29-37, preparing's & attachm
    msg = MIMEBase(maintype, subtype)
    msg.set_payload(fp.read())
    fp.close()

    encoders.encode_base64(msg)
    msg.add_header("Content-Disposition", "attachment", filename=spreadsheet)
    m.attach(msg)  # attachment

    s = smtplib.SMTP("localhost")
    s.set_debuglevel(1)
    s.sendmail(from_addr, to_addr, m.as_string())
    s.quit()


if __name__ == '__main__':
    send_mail('ravi@localhost', 'training@localhost', 'a test mail with attach',
              'a test mail' * 22)

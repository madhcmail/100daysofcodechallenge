import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from_addr = os.environ.get('FROM_ADDRESS')
to_addr = os.environ.get('TO_ADDRESS')
app_user = os.environ.get('GMAIL_APP_USER')
app_pwd = os.environ.get('GMAIL_APP_SECRET')

msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = "New Releases and Sales on Steam"

body = """New Releases and Sales on Steam

Click the links below to check them out!

"""

msg.attach(MIMEText(body, 'plain'))

smtp_server = smtplib.SMTP('smtp.gmail.com', 587)

smtp_server.ehlo()

smtp_server.starttls()

smtp_server.login(app_user, app_pwd)

text = msg.as_string()

smtp_server.sendmail(from_addr, to_addr, text)

smtp_server.quit()

print("Email sent successfully")

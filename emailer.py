import smtplib
import os

from_addr = os.environ.get('FROM_ADDRESS')
to_addr = os.environ.get('TO_ADDRESS')
app_user = os.environ.get('GMAIL_APP_USER')
app_pwd = os.environ.get('GMAIL_APP_SECRET')

body = """New Releases and sales on Steam.

Click the links below to check them out!

"""

# set up of smtp server
smtp_server = smtplib.SMTP('smtp.gmail.com', 587)

smtp_server.ehlo()  # sending a hello message to server and see if it responds

smtp_server.starttls()  # start encryption

smtp_server.login(app_user, app_pwd) # user the gmail id and the app_password that created in your account

smtp_server.sendmail(from_addr, to_addr, body)

smtp_server.quit()

print('Email sent Successfully...')



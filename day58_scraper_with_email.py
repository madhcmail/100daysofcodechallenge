import os
import bs4
import smtplib
import requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from_address = os.environ.get('FROM_ADDRESS')
to_address = os.environ.get('TO_ADDRESS')
app_user = os.environ.get('GMAIL_APP_USER')
app_pwd = os.environ.get('GMAIL_APP_SECRET')

msg = MIMEMultipart()
msg['From'] = from_address
msg['To'] = to_address
msg['Subject'] = "Fox Headlines"


URL = f"https://www.foxnews.com/"


# pull the site
def pull_site():
    raw_site_page = requests.get(URL)
    raw_site_page.raise_for_status()
    return raw_site_page


# scrape the site for the required details an convert into a string
def scrape(site):
    headers_list = []
    body = "Today's Headlines: \n\n"

    soup = bs4.BeautifulSoup(site.text, 'html.parser')
    html_header_list = soup.main.find_all('h2')

    for item in html_header_list:
        headers_list.append(item.getText())

    # convert the list into a string inorder to send it as a plain message though MIME email format
    for idx, header in enumerate(headers_list):
        body = body + str(idx+1) + '.' + header + '\n'
    return body

# function to send the Fox headlines to my email id
def send_mail(body_msg):

    body = body_msg

    msg.attach(MIMEText(body, 'plain'))

    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)

    smtp_server.ehlo()

    smtp_server.starttls()

    smtp_server.login(app_user, app_pwd)

    text = msg.as_string()

    smtp_server.sendmail(from_address, to_address, text)

    smtp_server.quit()

    print("Email sent successfully")


if __name__ == '__main__':
    site = pull_site()
    body_msg = scrape(site)  # get the headlines to send it through email
    send_mail(body_msg)  # call the email function

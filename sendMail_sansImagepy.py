# from myro import *

# enable sending function
import smtplib

# establish SMTP server and port
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

# modify sender, recipient
sender = 'og69loc@gmail.com'
recipient = 'michael.socha.99@hotmail.ca'

# create content of message
subject = 'Damn - my shit was whack!'
body = 'After five years on the east coast... It was time to go home.'
body = "" + body + ""
headers = ["From: " + sender,
           "Subject: " + subject,
           "To: " + recipient,
           "MIME-Version: 1.0",
           "Content-Type: text/html"]
headers = "\r\n".join(headers)

# send via SMTP server
session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
 
session.ehlo()
session.starttls()
session.ehlo()

session.login('og69loc@gmail.com', '$anFi3rro')
session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
session.quit()

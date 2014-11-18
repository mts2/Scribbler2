# enable sending/picture attaching function

def sendEmail(name, pictureString):

    import smtplib
    from email.MIMEImage import MIMEImage
    from email.MIMEMultipart import MIMEMultipart
    
    COMMASPACE = ', '
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587
    
    msg = MIMEMultipart()
    msg['Subject'] = 'The name of the burglar is ' + name + "."
    
    msg['From'] = 'og69loc@gmail.com'
    msg['To'] = COMMASPACE.join('og69loc@gmail.com')
    msg.preamble = 'The name of the burglar is '# + str(name) + "."  
    
    fp = open(pictureString, 'rb')
    img = MIMEImage(fp.read())
    fp.close()
    msg.attach(img)
    
    s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login('og69loc@gmail.com', '$anFi3rro')
    s.sendmail('og69loc@gmail.com', 'og69loc@gmail.com' , msg.as_string())
    s.quit()
    
    return
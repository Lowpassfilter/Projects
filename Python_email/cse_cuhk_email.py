#Copyright 2017 at Pengfei Liu. All Rights Reserved
#You may contact the author at liupengfei.leo@gmail.com

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from datetime import datetime


def SendMail(text):
    """This function is used to send email automatically using the email box from CSE CUHK, It should be executed in the CSE intronet """
    fromaddr = "your cse email address"
    toaddr = "destination email address"

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['to'] = toaddr
    msg['Subject'] = "Experiment finished at " + datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    body = "Dear Little Beauty\n\nCongratulations! Your experiments has finshed, here is the detials: \n" + text + "\n\nYours Sincerely\nHusband" 
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP('mail.cse.cuhk.edu.hk', 25)
    server.sendmail(fromaddr, toaddr, msg.as_string())
    server.quit()


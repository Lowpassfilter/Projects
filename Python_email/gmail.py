#Copyright 2017 at Pengfei Liu. All Rights Reserved
#You can contact the author from liupengfei.leo@gmail.com

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from datetime import datetime


def SendMail(text):
    """This function is used to send email from your gmail automatically. You need to enable the SMTP service in your gmail account first"""

    fromaddr = "Your gmail address"
    toaddr = "destination address"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['to'] = toaddr
    msg['Subject'] = "Experiment finished at " + datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    body = "Dear Little Beauty\n\nCongratulations! Your experiments has finshed, here is the detials: \n" + text + "\n\nYours Sincerely\nHusband" 
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(fromaddr,"your gmail password")

    server.sendmail(fromaddr, toaddr, msg.as_string())
    server.quit()


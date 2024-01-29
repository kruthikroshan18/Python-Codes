# Import smtplib and email modules
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Create an SMTP object
smtp = smtplib.SMTP('smtp.gmail.com', 587)

# Identify yourself to the server
smtp.ehlo()
#hiii

# Start encryption
smtp.starttls()

# Log in to your email account
smtp.login('.com', 'your_password')

# Create a MIMEMultipart object
msg = MIMEMultipart()

# Set the headers
msg['Subject'] = 'Hello from Python'
msg['From'] = 'your_email@gmail.com'
msg['To'] = 'receiver_email@gmail.com'

# Add the body
msg.attach(MIMEText('This is a test email', 'plain'))

# Send the email
smtp.sendmail('your_email@gmail.com', 'receiver_email@gmail.com', msg.as_string())

# Close the connection
smtp.quit()

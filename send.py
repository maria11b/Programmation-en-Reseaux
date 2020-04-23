import smtplib
from email.mime.text import MIMEText

smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465
username = 'mariabuftea2904@gmail.com'
password = 'pass'
sender = 'mariabuftea2904@gmail.com'
targets = ['bufteaelena@gmail.com', 'maria.buftea@ee.utm.md']

msg = MIMEText('Laboratorul Nr.2')
msg['Subject'] = 'Programarea in Retea '
msg['From'] = sender
msg['To'] = ', '.join(targets)

server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
server.login(username, password)
server.sendmail(sender, targets, msg.as_string())
server.quit()
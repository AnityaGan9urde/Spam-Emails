import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Anonymous'
email['to'] = '#Receiver''s email'
email['subject'] = '#message'

email.set_content(html.substitute({'name': 'Tintin'}),'html')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('#Your email', '#Your password')
    smtp.send_message(email)
    print('all good ')

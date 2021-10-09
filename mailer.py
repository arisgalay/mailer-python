import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['Subject'] = 'Python email module'
email['From'] = 'your@gmail.com'
email['To'] = 'send_to@outlook.com'

email.set_content('This email has been send thru python script.')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('your@gmail.com', 'stong_pw')
    smtp.send_message(email)
    smtp.quit()
    print('Email has been sent!')

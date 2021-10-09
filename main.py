from mailer import Mailer
# pip install quick-mailer
# https://pypi.org/project/quick-mailer/

mail = Mailer(email='your@gmail.com', password='strong_pw')
sender = 'your@gmail.com'
receivers = ['reciever1@outlook.com', 'reciever2@gmail.com']
body_message = 'Just sending an e-mail using python script!'

if mail.status:
    mail.send(receiver=receivers,
              subject='Quick mailer python library', message=body_message)

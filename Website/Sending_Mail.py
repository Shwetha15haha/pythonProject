import smtplib
import ssl


def send_mail(message):
    host = 'smtp.gmail.com'
    port = 465
    username = 'mogheshwetha15@gmail.com'
    password = 'XXXX'
    receiver = 'mogheshwetha15@gmail.com'

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


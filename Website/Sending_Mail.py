import smtplib
import ssl

host = 'smtp.gmail.com'
port = 465

username = 'mogheshwetha15@gmail.com'
password = 'lgjw bzxr kfmm qrmv'

receiver = 'mogheshwetha15@gmail.com'

message = """\
Subject:Hi
How are you?
Bye.
"""

context = ssl.create_default_context()

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)


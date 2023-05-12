import smtplib
import ssl
import os

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    context = ssl.create_default_context()

    password = os.getenv("portfolio_website_password")
    sender = "insmartdatascience@gmail.com"
    receiver = "insmartdatascience@gmail.com"

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)

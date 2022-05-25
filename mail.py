
import smtplib, ssl



def mail():
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "Abdullah@dextersol.com"
    receiver_email = ["adnan1470369258@gmail.com"]
    password = "lsoiinbshzynrtub"
    message = f"Subject: Test Mail Sent."
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    print("Email Sent succesfully...")



mail()

import os
from time import sleep
from datetime import datetime
import smtplib, ssl
import shutil


def delete():
    files = os.popen('find . -type f -name "*.log"').read().split('\n')[0:-1]
    files1 = os.popen('find . -type f -name "*.log.1"').read().split('\n')[0:-1]
    for count, file in enumerate(files):
        print(f"{count}: {file}")
        if os.path.exists(file) and os.path.splitext(file)[-1] == '.log':
            os.remove(file)
            print(f"File removed: {file}")
        else:
            print(f"File not removed: {file}")
    for count, file in enumerate(files1):
        print(f"{count}: {file}")
        print(f"{count}: {file}")
        if os.path.exists(file) and '.log.1' in file.split('/')[-1]:
            os.remove(file)
            print(f"File removed: {file}")
        else:
            print(f"File not removed: {file}")


def mail():
    dir = os.listdir("/home/user-data/mail/mailboxes")
    total, used, free = shutil.disk_usage("/")
    total1 = ("Total: %d GiB" % (total // (2**30)))
    used1 = ("Used: %d GiB" % (used // (2**30)))
    free1 = int(free//(2**30))
    if free1 < 235:
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = "adnan1470369258@gmail.com"
        receiver_email = ["adnan1470369258@gmail.com", "sufyansajid01@gmail.com"]
        password = "bhjnxdwguzrwzkqw"
        message = f"Subject: Disk Usage Alert.This message is sent from your Server: {dir[0]} And {total1}, {used1}, Free Space: {free1} GiB."
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        print("Email Sent succesfully...")
    else:
        print(f"Email Not Sent Because Used Space Is Less Then 16: {free1}")



i = 1
while True:
    today = datetime.now()
    d1 = today.strftime('%Y/%m/%d %I:%M:%S %p')
    print(f"\n{i}: Run.. On {d1}\n")
    delete()
    print("Thanks For Using The Function...\n")
    mail()
    i+=1
    sleep(43200)




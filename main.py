from time import sleep
from datetime import datetime
import smtplib, ssl, os, shutil, json, time


def delete():
    files = os.popen('find . -type f -name "*.log"').read().split('\n')[0:-1]
    files1 = os.popen('find . -type f -name "*.log.1"').read().split('\n')[0:-1]
    for count, log in enumerate(files):
        print(f"{count}: {log}")
        if os.path.exists(log) and os.path.splitext(log)[-1] == '.log':
            os.remove(log)
            print(f"File removed: {log}")
            

    for count, log1 in enumerate(files1):
        print(f"{count}: {log1}")
        if os.path.exists(log1) and '.log.1' in log1.split('/')[-1]:
            os.remove(log1)
            print(f"File removed: {log1}")
    
    # dir = os.listdir("/home/user-data/mail/mailboxes")
    # mailers = os.path.join("/home/user-data/mail/mailboxes", dir[0])
    # dir2 = os.listdir(mailers)
    # for file in dir2:
    #     if os.path.exists(os.path.join(mailers, file)):
    #         try:
    #             os.rmdir(os.path.join(mailers, file))
    #             print(f"File removed: {file}")
    #         except OSError:
    #             try:
    #                 os.system("rm -rf %s" % os.path.join(mailers, file))
    #                 print(f"File removed: {file}")
    #             except:
    #                 print('While Removing The Directory, An Error Occured')


    syslog = "/var/log"
    if os.path.exists(os.path.join(syslog, "syslog")):
        os.remove(os.path.join(syslog, "syslog"))
        print('Syslog Removed.')
    if os.path.exists(os.path.join(syslog, "syslog.1")):
        os.remove(os.path.join(syslog, "syslog.1"))
        print('Syslog.1 Removed.')
    if os.path.exists(os.path.join(syslog, "syslog.2.gz")):
        os.remove(os.path.join(syslog, "syslog.2.gz"))
        print('Syslog.2.gz Removed.')
    if os.path.exists(os.path.join(syslog, "syslog.3.gz")):
        os.remove(os.path.join(syslog, "syslog.3.gz"))
        print('Syslog.3.gz Removed.')
    if os.path.exists(os.path.join(syslog, "syslog.4.gz")):
        os.remove(os.path.join(syslog, "syslog.4.gz"))
        print('Syslog.4.gz Removed.')
    if os.path.exists(os.path.join(syslog, "syslog.5.gz")):
        os.remove(os.path.join(syslog, "syslog.5.gz"))
        print('Syslog.5.gz Removed.')
    if os.path.exists(os.path.join(syslog, "syslog.6.gz")):
        os.remove(os.path.join(syslog, "syslog.6.gz"))
        print('Syslog.6.gz Removed.')
    if os.path.exists(os.path.join(syslog, "syslog.7.gz")):
        os.remove(os.path.join(syslog, "syslog.7.gz"))
        print('Syslog.7.gz Removed.')

    
    if os.path.exists(os.path.join(syslog, "mail.log")):
        os.remove(os.path.join(syslog, "mail.log"))
        print('mail.log Removed.')
    if os.path.exists(os.path.join(syslog, "mail.log.1")):
        os.remove(os.path.join(syslog, "mail.log.1"))
        print('mail.log.1 Removed.')



def usage():
    context = {}
    total, used, free = shutil.disk_usage("/")
    total1 = ("Total: %d GB" % (total // (2**30)))
    used1 = ("Used: %d GB" % (used // (2**30)))
    free1 = int(free//(2**30))
    dir = os.listdir("/home/user-data/mail/mailboxes")
    context.update({
        "total": total1,
        "used": used1,
        "free": free1,
        'dir': dir[0]
    })
    return context



def check_reboot():
    with open('info.json', 'r') as f:
        info = json.load(f)
    interval = int(time.time() - info['time'])
    if interval > 1200:
        with open('info.json', 'w') as f:
            json.dump({'time': time.time()}, f)
        return True
    else:
        return False


def send_mail(message):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "adnan1470369258@gmail.com"
    receiver_email = ["adnan1470369258@gmail.com"]
    password = "wuwytstulqkyjkhv"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)




def mail():
    context = usage()
    if context.get('free') < 10:
        message = f"Subject: Disk Usage. Server: {context.get('dir')} And {context.get('total')}, {context.get('used')}, Free Space: {context.get('free')} GB, Restarting."
        send_mail(message)
        if check_reboot():
            sleep(4)
            os.system('sudo reboot')







def server_up():
    context = usage()
    message = f"Subject: Disk Usage Reboot, Server: {context.get('dir')} And {context.get('total')}, {context.get('used')}, Free Space: {context.get('free')} GB, Restarted."
    send_mail(message)
    sleep(4)




server_up()
i = 1
while True:
    today = datetime.now()
    d1 = today.strftime('%Y/%m/%d %I:%M:%S %p')
    print(f"\n{i}: Run.. On {d1}\n")
    delete()
    print("Thanks For Using The Function...\n")
    mail()
    i+=1
    sleep(21600)




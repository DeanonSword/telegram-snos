import os
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import datetime
from tqdm import tqdm

def sendemail(senderemail, senderpassword, recipientemail, subject, messagetext, attachments=None):
    try:
        server = smtplib.SMTP('smtp.mail.ru', 587)
        server.starttls()
        server.login(senderemail, senderpassword)

        message = MIMEMultipart()
        message['From'] = senderemail
        message['To'] = recipientemail
        message['Subject'] = subject

        body = messagetext
        message.attach(MIMEText(body, 'plain'))
        server.send_message(message)
        now = datetime.datetime.now()
        print(f"[{now.strftime('%H:%M:%S')}] Письмо от {senderemail} успешно отправлено на {recipientemail}.")

        server.quit()
    except Exception as e:
        print(f"Ошибка при отправке письма: {str(e)}")


logo = """
_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_
rimuru & osimtet and Paranormal Liberation 

koder: Fazzit (@fazzyt)
helper: rimuru (@lol_i_rimuru)

[+] V-Beta
[+] обновления будут
[+] за копирование дадим пизды 
[+] ньюфагам которые не шарят за норм снос - дорога нахуй 
_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_
правила использования:
[+] все жалобы должны быть не за просто так 
[+] писать желательно на английском 
[+] жалобы только по фактам иначе тг вам нахуй пошлет
[+] пример отправки письма в файле README.TXT
_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_
если заметили не доработку или ошибку, то пишите :
@lol_i_rimuru

все кроме нас.
а чë сразу мы?

"""


if __name__ == "__main__": 
    recipients = ["abuse@telegram.org", "Spam@telegram.org"]
    senders = []
    
    with open("mail.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            email, password = line.strip().split(":")
            senders.append((email, password))

    print(logo)
    subject = str(input("[AC] название письма > "))
    messagetext = str(input("[AC] текст письма > "))

    
    for senderemail, senderpassword in senders:
        for recipientemail in recipients:
            sendemail(senderemail, senderpassword, recipientemail, subject, messagetext)
            for _ in tqdm(range(100)):
                pass
            time.sleep(300);

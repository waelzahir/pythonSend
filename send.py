import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import re
import time
import csv

LETTER = "letter.txt"
ADRESSES = "adresses.csv"
PDFFILE = "pdfile.pdf"
lettertext = open(LETTER, "r").read()
csvfile = csv.reader(open(ADRESSES), delimiter='\n')



def startserver (username, password):
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    return server

def get_msg(reciever, subject, filename, row) :
    msg = MIMEMultipart()
    msg['To'] = reciever
    msg['From'] = "Ouail Zahir <contact@waelzahir.me>"
    msg['Subject'] = subject

    msg.attach(MIMEText(lettertext))
    payload = MIMEBase('application', 'octate-stream', Name=filename)
    payload.set_payload((open(filename, "rb")).read())
    encoders.encode_base64(payload)
    payload.add_header('Content-Decomposition', 'attachment', filename=filename)
    msg.attach(payload)
    return msg



def start(csvfile):
    mainaddr = ''
    password =  open(".env", "r").read()
    server = startserver(mainaddr, password)
    for row in csvfile:
        time.sleep(60)
        reciever = row[0]
        fromaddr = 'contact@waelzahir.me'
        msg = get_msg( "<" + reciever + ">", "", PDFFILE , row)
        server.sendmail(fromaddr, reciever,  msg.as_string())
    server.quit()




start(csvfile)
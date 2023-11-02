import smtplib
import ssl
from password import *

port=587
ser='smtp.gmail.com'

fromm="saadzh7@gmail.com"

rec=input("enter the receiving mail id")
pswd=password


sub=input("enter the subject:")
body=input("enter the body of the message")
msg="Subject:{}\n\n{}".format(sub,body)
cont=ssl.create_default_context()

try:
    print("Connecting yo thr server,...")
    server=smtplib.SMTP(ser,port)
    server.starttls(context=cont)
    server.login(fromm,pswd)
    print("Connected yo thr server...")
    print()

    print(f"sending email to {rec}")
    server.sendmail(fromm,rec,msg)
    print(f"successfully sent  email to {rec}")
except Exception as e:
    print(e)

finally:
    server.quit()
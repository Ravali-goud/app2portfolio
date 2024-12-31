import smtplib,ssl

def send_email(message):
    host="smtp.gmail.com"
    port=465

    username="gravali919@gmail.com"
    password="eijmzdiyhvofrrer"

    receiver="gravali919@gmail.com"
    context=ssl.create_default_context()

    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,message)
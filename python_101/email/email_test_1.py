import smtplib

HOST = "mySMTP.server.com"
SUBJECT = "Hello There"
TO = "afoglema@gmail.com"
FROM = "Pytest@hello.com"
text = "Hello from the smtp module"


def send_email(host, subject, to_addr, from_addr, body_text):
    BODY = "\r\n".join((
        "From: %s" % FROM,
        "To: %s" % TO,
        "Subject: %s" % SUBJECT,
        "",
        text
    ))

    server = smtplib.SMTP(HOST)
    server.sendmail(FROM, [TO], BODY)
    server.quit()

if __name__ == "__main__":
    send_email(HOST, SUBJECT, TO, FROM, text)

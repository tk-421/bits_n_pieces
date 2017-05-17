import os
import smtplib
import sys

from configparser import ConfigParser

def send_email(subject, to_addr, body_text):
    # Send an email using config file properties

    base_path = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_path, "email.ini")

    if os.path.exists(config_path):
        cfg = ConfigParser()
        cfg.read(config_path)
    else:
        print("No Config file found, exiting.")
        sys.exit(1)

    host = cfg.get("smtp", "server")
    from_addr = cfg.get("smtp", "from_addr")

    BODY = "\r\n".join((
        "From: %s" % from_addr,
        "To: %s" % to_addr,
        "Subject: %s" % subject,
        "",
        body_text
    ))
    server = smtplib.SMTP(host)
    server.sendmail(from_addr, [to_addr], BODY)
    server.quit()

    if __name__ == "__main__":
        subject = "Test email from python"
        to_addr = "afoglema@gmail.com"
        body_text = "Hello from python smtplib"
        send_email(subject, to_addr, body_text)

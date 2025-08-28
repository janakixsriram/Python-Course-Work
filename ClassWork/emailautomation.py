import smtplib #simple mail transfer protocol for sending mails
import os #for file path and file existence checks
import csv #csv to read email addresses from a cs
from email.mime.multipart import MIMEMultipart
# For creating.mime.text import MIMEText
# for adding plain text to email body
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587 #PORT USED FOR TLS (ENCRYPTION)
SENDER_EMAIL = "sriramsegu2003@gmail.com"
SENDER_PASSWORD = "pzfm niqj xkpc s"

def send_email (to_email, subject, body):
    try:
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = to_email
        msg["subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP(SMTP_SERVER,SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, to_email, msg.as_string())
        server.quit()

        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"error sending email to {to_email}: {e}")

    def send_bulk_emails(csv_file, subject, body):
        try:
            csv_path = os.path.abspath(csv_file)
            if not os.path.exists(csv_path):
                print(f"Error: CSV file'{csv_file}' not found.")
                return
with open(csv_path, newline = "",encoding = "utf-8") as file:



    reader = csv.reader(file)
    next(reader, None)
    print(reader,"reader")
    for row in reader:
        

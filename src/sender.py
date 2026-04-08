import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# smtplib     → talks to the email server (SMTP protocol)
# MIMEMultipart → the email "envelope" container
# MIMEText      → the text that goes inside the envelope

def send_mail(smtp_server, smtp_port, sender_email, password, recipient_email, subject, body):
    try:
        # Build the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Open TCP connection → upgrade to encrypted (TLS) → login → send
        server = smtplib.SMTP(smtp_server, smtp_port, timeout=15)
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)
        server.quit()
        return True, "Email sent successfully!"

    except Exception as e:
        return False, f"SMTP Error: {str(e)}"
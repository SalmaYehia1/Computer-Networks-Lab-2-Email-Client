import imaplib
import email
from plyer import notification

# imaplib      → connects to and reads from email servers (IMAP protocol)
# email        → parses raw email bytes into readable parts
# plyer        → sends desktop pop-up notifications

def fetch_latest_email(imap_server, imap_port, email_user, password):
    try:
        # Connect, login, open inbox
        mail = imaplib.IMAP4_SSL(imap_server, imap_port)
        mail.login(email_user, password)
        mail.select("inbox")

        # Get list of all email IDs
        status, data = mail.search(None, "ALL")
        mail_ids = data[0].split()
        if not mail_ids:
            return "No emails found."

        # Fetch the most recent one (last ID in the list)
        status, data = mail.fetch(mail_ids[-1], "(RFC822)")
        msg = email.message_from_bytes(data[0][1])

        # Extract plain-text body (emails can have multiple parts)
        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode().replace('\r\n', '\n').strip()
                    break
        else:
            body = msg.get_payload(decode=True).decode().replace('\r\n', '\n').strip()

        # Desktop notification
        notification.notify(
            title=f"New Email: {msg['Subject']}",
            message=f"From: {msg['From']}",
            app_name="Email Client",
            timeout=10
        )

        mail.close()    # close the selected mailbox
        mail.logout()   # then disconnect from the server
        return f"From: {msg['From']}\nSubject: {msg['Subject']}\nBody:\n{body}"

    except Exception as e:
        return f"IMAP Error: {str(e)}"
# Computer-Networks-Lab-2-Email-Client

Alexandria University – Computer Networks (Faculty of Engineering). Lab 2 implementing a Python-based email client with a tkinter GUI, capable of sending emails via SMTP and retrieving inbox messages via IMAP, with desktop notifications using the plyer library.

---

## Objective

Develop a functional Python-based email client featuring a graphical user interface (GUI) capable of:
- **Sending** emails using the Simple Mail Transfer Protocol (SMTP)
- **Retrieving** the most recent inbox email using the Internet Message Access Protocol (IMAP)

---

## Project Structure

```
├── README.md
└── src/
    ├── main.py         # tkinter GUI — captures user input and coordinates send/receive logic
    ├── sender.py       # Outbound email logic via SMTP (smtp.gmail.com:587, STARTTLS)
    └── receiver.py     # Inbound email logic via IMAP (imap.gmail.com:993, SSL) + desktop notification
```

---

## System Architecture

| Module | Responsibility |
|---|---|
| `main.py` | Builds the UI using `tkinter`, pre-fills test credentials, bridges sender and receiver modules |
| `sender.py` | Constructs email using `email.mime`, connects via `smtplib` with TLS encryption |
| `receiver.py` | Connects via `imaplib` over SSL, fetches latest email using RFC822, triggers `plyer` notification |

---

## Getting Started

### Prerequisites

Most dependencies are part of the Python Standard Library (`tkinter`, `smtplib`, `imaplib`, `email`).  
Install the only external dependency:

```bash
pip install plyer
```

### Gmail App Password Setup

Standard Gmail passwords are rejected due to Google's security policies.  
You must generate a **Google App Password**:

1. Go to your Google Account → Security → App Passwords
2. Generate a password for "Mail"
3. Use this password in the App Password field

> The app has a test account hard-coded for immediate testing convenience.

### Running the App

Navigate to the `src/` directory and run:

```bash
cd src
python main.py
```

---

## Test Cases

| Test Case | Result |
|---|---|
| GUI Initialization | GUI launches with hard-coded test parameters pre-filled |
| Sending an Email | Successfully connected to SMTP server and returned success prompt |
| Fetching Latest Email | Retrieved latest email via IMAP, displayed in inbox, triggered desktop notification |

---

## Key Findings

1. **Protocol Roles** — SMTP is a push-only protocol; IMAP is a pull/sync protocol. Both are needed for a complete client.
2. **Security** — `STARTTLS` is required for SMTP; `IMAP4_SSL` for IMAP. App Passwords replace standard credentials.
3. **Latency** — SMTP sends execute faster than IMAP fetches, as IMAP must load the mailbox, search message IDs, and fetch raw byte structures.

---

## Technologies Used

- **Python** — Core language
- **tkinter** — GUI framework
- **smtplib** — SMTP email sending
- **imaplib** — IMAP email retrieval
- **email / email.mime** — Email construction and parsing
- **plyer** — Cross-platform desktop notifications

---


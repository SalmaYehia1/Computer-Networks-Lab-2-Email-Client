import tkinter as tk
from tkinter import messagebox, scrolledtext

# Import the logic functions from the other two files
from sender import send_mail
from receiver import fetch_latest_email

# Server configuration (Gmail)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT   = 587
IMAP_SERVER = "imap.gmail.com"
IMAP_PORT   = 993


def send_email_logic():
    success, message = send_mail(
        SMTP_SERVER, SMTP_PORT,
        entry_user.get(), entry_pw.get(),
        entry_to.get(), entry_sub.get(),
        text_body.get("1.0", tk.END)
    )
    if success:
        messagebox.showinfo("Success", message)
    else:
        messagebox.showerror("Error", message)

def receive_email_logic():
    result = fetch_latest_email(IMAP_SERVER, IMAP_PORT, entry_user.get(), entry_pw.get())
    text_display.delete("1.0", tk.END)
    text_display.insert(tk.END, result)

# --- GUI SETUP ---
root = tk.Tk()
root.title("Email Client - Lab 2")
root.geometry("500x650")

tk.Label(root, text="Gmail Address:", font=('Arial', 10, 'bold')).pack(pady=2)
entry_user = tk.Entry(root, width=40)
entry_user.insert(0, "salmayehia155@gmail.com")
entry_user.pack()

tk.Label(root, text="App Password:", font=('Arial', 10, 'bold')).pack(pady=2)
entry_pw = tk.Entry(root, width=40, show="*")
entry_pw.insert(0, "kzix syex vczh smux")
entry_pw.pack()

tk.Label(root, text="Recipient Email:", font=('Arial', 10, 'bold')).pack(pady=2)
entry_to = tk.Entry(root, width=40)
entry_to.insert(0, "salmayehia155@gmail.com")
entry_to.pack()

tk.Label(root, text="Subject:", font=('Arial', 10, 'bold')).pack(pady=2)
entry_sub = tk.Entry(root, width=40)
entry_sub.pack()

tk.Label(root, text="Email Body:", font=('Arial', 10, 'bold')).pack(pady=2)
text_body = tk.Text(root, height=5, width=40)
text_body.pack()

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)
tk.Button(btn_frame, text="Send Email",   command=send_email_logic,    bg="#4CAF50", fg="white", width=15).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Fetch Latest", command=receive_email_logic, bg="#2196F3", fg="white", width=15).grid(row=0, column=1, padx=5)

tk.Label(root, text="Inbox Display:", font=('Arial', 10, 'bold')).pack(pady=5)
text_display = scrolledtext.ScrolledText(root, height=10, width=50, bg="#f0f0f0")
text_display.pack(pady=5)

root.mainloop()
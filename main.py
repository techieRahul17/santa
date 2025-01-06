import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random


def send_email(sender_email, receiver_email, subject, body, password):
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            print(f"Email sent to {receiver_email}!")
    except Exception as e:
        print(f"Failed to send email to {receiver_email}. Error: {e}")


emails = [
    'shailesh2310592@ssn.edu.in',
    'pranav2310279@ssn.edu.in',
    'anjalimani2310526@ssn.edu.in',
    'balamurugan2310242@ssn.edu.in',
    'rahul2310239@ssn.edu.in',
    'dakshata2310540@ssn.edu.in',
]

names = ['shailesh', 'pranav', 'anjali', 'rahul', 'dakshata', 'bala']

def assign_and_send():
    sender_email = 'exoweb1899@gmail.com'
    password = 'lbbq aftl clho oywh'  # Use your actual app password here

    # Ensure the lists are of the same length
    if len(emails) != len(names):
        print("Error: Email and name list lengths don't match!")
        return

    # Ensure fresh shuffle each time
    shuffled_names = names.copy()

    # Optional: Set a random seed for true randomness if needed
    random.seed()  # This uses the current system time or another source of entropy

    # Ensure no name appears in their own email
    while True:
        random.shuffle(shuffled_names)
        valid = True
        for email, assigned_name in zip(emails, shuffled_names):
            if assigned_name.lower() in email.lower():
                valid = False
                break
        if valid:
            break

    # Send emails
    for email, assigned_name in zip(emails, shuffled_names):
        subject = f" testing Secret Santa Assignment! - pranav "
        body = f"Hello! You've been assigned to {assigned_name}."
        send_email(sender_email, email, subject, body, password)

# Run the assignment and email sending
assign_and_send()

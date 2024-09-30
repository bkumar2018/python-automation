import smtplib

sender = "your_email@example.com"
receiver = "recipient@example.com"
subject = "Automated Email"
body = "This is an automated email sent using Python."

message = f"Subject: {subject}\n\n{body}"

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.starttls()
    smtp.login("your_email@example.com", "your_password")
    smtp.sendmail(sender, receiver, message)



# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# # Email details
# sender_email = "your_email@example.com"
# receiver_email = "recipient@example.com"
# subject = "Automated Email"
# body = "This is a test email sent from Python automation script."

# # Create message
# msg = MIMEMultipart()
# msg['From'] = sender_email
# msg['To'] = receiver_email
# msg['Subject'] = subject
# msg.attach(MIMEText(body, 'plain'))

# # Login and send the email
# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls()
# server.login(sender_email, "your_password")
# server.sendmail(sender_email, receiver_email, msg.as_string())
# server.quit()

# print("Email sent successfully!")

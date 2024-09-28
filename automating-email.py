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

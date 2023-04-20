import smtplib

sender_email = 'your-email@example.com'
receiver_email = ['list1@example.com', 'list2@example.com']
password = 'your-password'
subject = 'CentOS server update report'
message = 'Here is the update report for the CentOS servers:'

try:
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, f'Subject: {subject}\n\n{message}')
    print('Email sent successfully.')
except Exception as e:
    print(f'Error sending email: {e}')

"""
    @summary SMTP connection details
    @author Sathya Sai M
    @since November 2019
"""


from email.mime.multipart import MIMEMultipart
import smtplib, os


def smtp(email_id):
    msg = MIMEMultipart()
    # setup the parameters of the message
    password = os.getenv("SMTP_EXCHANGE_USER_PASSWORD")
    msg['From'] = os.getenv("SMTP_EXCHANGE_USER_LOGIN")
    msg['To'] = email_id
    msg['Subject'] = "Subscription"
    # add in the message body
    server = smtplib.SMTP('os.getenv("SMTP_EXCHANGE_SERVER"): os.getenv("SMTP_EXCHANGE_PORT")')
    server.starttls()
    # Login Credentials for sending the mail
    server.login(msg['From'], password)
    # send the message via the server.
    server.sendmail(msg['From'], [msg['To']], msg.as_string())
    server.quit()
    print("successfully sent email to %s:" % (msg['To']))
    server.quit()


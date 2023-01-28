from email.message import EmailMessage
from os import getenv
from smtplib import SMTP_SSL

from dotenv import load_dotenv

####################################################################################################

# create the email message
def create_email_message(subject: str, recipient: str, receiver: str, message: str) -> EmailMessage:
    email_msg = EmailMessage()

    email_msg["Subject"] = subject
    email_msg["From"] = recipient
    email_msg["To"] = receiver

    email_msg.set_content(message)

    return email_msg

# send the email
def send_email(email: str, password: str, email_msg: EmailMessage) -> None:
    protocol = SMTP_SSL("smtp.gmail.com", 465)

    try:
        protocol.login(email, password)
        protocol.send_message(email_msg)
    except Exception as e:
        print(e)
    finally:
        protocol.quit()

# main method
def main():
    # load environment variables
    load_dotenv()

    # get the email address and password for authentication
    email = getenv("EMAIL")
    password = getenv("PASSWORD")

    # create the email message and send it
    email_msg = create_email_message("", "", "", "")
    send_email(email, password, email_msg)

# execute main method
if __name__ == "__main__":
    main()

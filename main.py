from os import getenv

from dotenv import load_dotenv

from email_alert import create_email_message, send_email

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

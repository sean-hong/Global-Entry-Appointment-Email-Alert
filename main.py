from os import getenv

from dotenv import load_dotenv

from email_alert import create_email_message, send_email
from global_entry_api import call_api, read_api_data

# main method
def main():
    # load environment variables
    load_dotenv()

    # get the environment stuff
    env_email = getenv("EMAIL")
    env_password = getenv("PASSWORD")
    location_id = int(getenv("LOCATION"))

    # get the soonest appointment info from the airport
    appointment_info = call_api(location_id)

    # make sure that the appointment is available
    if appointment_info is not None:
        # set the email parameters
        subject = "Global Entry Appointment"
        sender = env_email
        receiver = env_email
        message = read_api_data(location_id, appointment_info)

        # create the email message and send it
        email_msg = create_email_message(subject, sender, receiver, message)
        send_email(env_email, env_password, email_msg)

        print("Email sent")
    else:
        print("No appointment spots available")

# execute main method
if __name__ == "__main__":
    main()

# install requirements
from twilio.rest import Client
from datetime import datetime, timedelta
import time

# get twilio credentials
account_sid = ""
auth_token = ""


client = Client(account_sid, auth_token)

# message sender function


def send_whatsapp_message(recipent_number, message_body):
    try:
        message = client.messages.create(
            from_="whatsapp:",  # add the twilio number here to run the program again
            body=message_body,
            to=f"whatsapp:{recipent_number}",
        )
        print(f"Message sent successfully! Message Sid{message.sid}")
    except Exception as e:
        print("An error occured")


# taking user input
name = input("Enter Recipent name: ")
recipent_number = input(
    "Enter the recipent whatsapp number with country code (eg:+12345): "
)
message_body = input(f"Enter the message you want to send to {name}: ")


# date and time and calculate delay
date_str = input(
    "Enter date on which you want to send the message(format: YYYY-MM-DD): "
)
time_str = input(
    "Enter the on which you want to send this message(format:HH:MM 24 hour format): "
)

# datetime

schedule_datetime = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
current_datetime = datetime.now()

# calculate delay
time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()


if delay_seconds <= 0:
    print("Given date and time is in the past so unable to send the message")

else:
    print(f"Message scheduled to be sent to {name} on {schedule_datetime}. ")

    # wait until the schedule time
    time.sleep(delay_seconds)

    # send the message
    send_whatsapp_message(recipent_number, message_body)

# import base64
# from email.mime.text import MIMEText
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# from requests import HTTPError lmyzmctmrdydohdg


# SCOPES = [
#         "https://www.googleapis.com/auth/gmail.send"
#     ]
# flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
# creds = flow.run_local_server(port=0)

# service = build('gmail', 'v1', credentials=creds)
# # message = MIMEText('This is the body of the email')
# body = """
# Hey y’all,

# Please update the google doc for this Wednesday's game: https://tinyurl.com/1spatial
# And check here for any debt: https://docs.google.com/spreadsheets/d/1ozb59B-EGwDfrgqMtm9dEeD34PM0Bff7jReJx9duENs/edit?usp=sharing 

# Cheers,

# Dolphy

# """
# message = MIMEText(body, 'html')
# message['to'] = 'dolphy@aliases.me'
# message['subject'] = 'Email Subject'
# create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

# try:
#     message = (service.users().messages().send(userId="me", body=create_message).execute())
#     print(F'sent message to {message} Message Id: {message["id"]}')
# except HTTPError as error:
#     print(F'An error occurred: {error}')
#     message = None

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from datetime import datetime, timedelta

def nextWednesday():
   # Get the current date
   now = datetime.now()

   # Get the weekday number for today (0 is Monday, 1 is Tuesday, ..., 6 is Sunday)
   weekday = now.weekday()

   # Calculate how many days we have to add to get to the next Wednesday
   # The number 2 represents Wednesday (0 for Monday, 1 for Tuesday, etc.)
   days_until_wednesday = (2 - weekday + 7) % 7

   if days_until_wednesday == 0:
       # If today is Wednesday, get the next Wednesday
       days_until_wednesday = 7

   # Add the necessary number of days to the current date
   next_wednesday = now + timedelta(days=days_until_wednesday)

   # Print the result
   print('The next Wednesday is on:', next_wednesday)
   return next_wednesday.strftime('%d-%B-%Y')



def send_email(subject, body, sender, recipients, password):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    part1 = MIMEText(body, 'html')
    msg.attach(part1)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")

if __name__ == "__main__":

   subject = "[footy5aside] Game on " + nextWednesday()
   body = """
   <html>
   <body>
         <p>Hey y’all,</p>

         <p>Please update the google doc for this Wednesday's game: <a href="https://tinyurl.com/1spatial">https://tinyurl.com/1spatial</a></p>
         <p>And check here for any debt: <a href="https://docs.google.com/spreadsheets/d/1ozb59B-EGwDfrgqMtm9dEeD34PM0Bff7jReJx9duENs/edit?usp=sharing">https://docs.google.com/spreadsheets/d/1ozb59B-EGwDfrgqMtm9dEeD34PM0Bff7jReJx9duENs/edit?usp=sharing</a></p>

         <p>Cheers,</p>
         <p>Dolphy</p>
   </body>
   </html>
         """
   sender = "dolphy.phanle@gmail.com"
   recipients = ["dolphy@aliases.me"]
   # Get password from environment variable
   password = os.environ.get("EMAIL_PASSWORD")
   send_email(subject, body, sender, recipients, password)
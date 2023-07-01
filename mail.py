import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

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

   load_dotenv()
   
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
   password = os.getenv('EMAIL_PASSWORD')
   send_email(subject, body, sender, recipients, password)
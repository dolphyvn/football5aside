import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from datetime import datetime, timedelta
from mail import send_email
from main import nextWednesday
from dotenv import load_dotenv


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
   recipients = (os.getenv('TOME')).split(',')
   send_email(subject, body, sender, recipients)
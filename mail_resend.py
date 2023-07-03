import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from datetime import datetime, timedelta
from mail import send_email
from main import nextWednesday
from dotenv import load_dotenv


def gameIsOnConfirm():

   load_dotenv()
   subject = "[footy5aside] Game on " + nextWednesday()
   body = """
   <html>
   <body>
         <p>Hi everyone,</p>

         <p>We have enough players: <a href="https://tinyurl.com/1spatial">https://tinyurl.com/1spatial</a></p>
         <p>So game is on today. See you!</p>

         <p>Cheers,</p>
         <p>Dolphy</p>
   </body>
   </html>
         """
   sender = "dolphy.phanle@gmail.com"
   recipients = (os.getenv('TONH')).split(',')
   send_email(subject, body, sender, recipients)


def gameIsOffConfirm():

   load_dotenv()
   subject = "[footy5aside] Game on " + nextWednesday()
   body = """
   <html>
   <body>
         <p>Hi everyone,</p>

         <p>We have not enough players: <a href="https://tinyurl.com/1spatial">https://tinyurl.com/1spatial</a></p>
         <p>So game is Off today. See you next week hopefully!</p>

         <p>Cheers,</p>
         <p>Dolphy</p>
   </body>
   </html>
         """
   sender = "dolphy.phanle@gmail.com"
   recipients = (os.getenv('TONH')).split(',')
   send_email(subject, body, sender, recipients)

def cancelBooking():

   load_dotenv()
   subject = "[footy5aside] Game on " + nextWednesday()
   body = """
   <html>
   <body>
         <p>Hi NH,</p>

         <p>We would like to cancel our booking today from 6pm to 7pm ( 1Spatial )</p>
         <p>Thank you very much!</p>

         <p>Cheers,</p>
         <p>Dolphy</p>
   </body>
   </html>
         """
   sender = "dolphy.phanle@gmail.com"
   recipients = (os.getenv('TOME')).split(',')
   send_email(subject, body, sender, recipients)
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from datetime import datetime, timedelta
from mail import send_email
from main import nextWednesday,currentWednesday
from dotenv import load_dotenv


def beforeGameDay(nplayers):

   load_dotenv()

   # Messages based on number of players
   if nplayers == 0:
      message = "We currently have no players. If you have friends and want to join, please share with them."
   elif nplayers <= 7:
      message = f"We currently have {nplayers}. We need more guys."
   elif nplayers < 9:
      message = "Looks like we have enough. Keep it up, guys!"
   elif nplayers < 12:
      message = "Great turnout! Looking forward to the game."
   else:
      message = "Fantastic! We have more than enough players. Let's make this a great game."

   subject = "[footy5aside] Game on " + nextWednesday()
   body = f"""
   <html>
   <body>
         <p>Hi everyone,</p>

         <p>Just another reminder to signup your name here: <a href="https://tinyurl.com/1spatial">https://tinyurl.com/1spatial</a> for the game tomorrow.</p>
         <p>{message}</p>

         <p>Cheers,</p>
         <p>Dolphy</p>
   </body>
   </html>
         """
   sender = "dolphy.phanle@gmail.com"
   recipients = (os.getenv('TONH')).split(',')
   send_email(subject, body, sender, recipients)

def gameIsOnConfirm():

   load_dotenv()
   subject = "[footy5aside] Game on " + currentWednesday()
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
   subject = "[footy5aside] Game OFF " + nextWednesday()
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
   subject = "[footy5aside] Game OFF " + nextWednesday()
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

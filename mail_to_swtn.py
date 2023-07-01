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
   subject = "Netherhall Football on " + nextWednesday()
   body = """
   <html>
   <body>
         <p>Hi everyone,</p>

         <p>Anyone would like to play footbal game on this Wednesday at 6pm at Netherhall Sports Center. </p>
         <p>Please update google spreadsheet if you interested: <a href="https://tinyurl.com/1spatial">https://tinyurl.com/1spatial</a></p>
         
         <p>Cheers,</p>
         <p>Dolphy</p>
   </body>
   </html>
         """
   sender = "dolphy.phanle@gmail.com"
   recipients = (os.getenv('TOSWT')).split(',')
   send_email(subject, body, sender, recipients)
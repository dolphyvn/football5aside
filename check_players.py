import gspread
from datetime import datetime, timedelta
import os
from mail import send_email
from dotenv import load_dotenv
from mail_resend import cancelBooking,gameIsOffConfirm,gameIsOnConfirm

def count(sh):

	worksheet = sh.worksheet("Live")
	# values_list = worksheet.col_values(3)
	cell_list = worksheet.get('C7:C20')
	values_list = [cell for sublist in cell_list for cell in sublist]

	return values_list






if __name__ == "__main__":
	# gc = gspread.service_account()
	gc = gspread.oauth(
	    credentials_filename=os.path.expanduser('~/.config/gspread/credentials.json'),
	    authorized_user_filename=os.path.expanduser('~/.config/gspread/authorized_user.json')
	)

	sh = gc.open("1Spatial Football - 2023")
	nplayers = (len(count(sh)))
	if int(nplayers) < 8:
		print("Game will cancel before 4pm")
		print("Sending cancel booking email to NH support staff")
		cancelBooking()
		print("Resend notification for players that game has been canceled")
		gameIsOffConfirm()
	else:
		print("Resend confirmation that game is on.")
		gameIsOnConfirm()


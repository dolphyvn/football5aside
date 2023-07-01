import gspread
from datetime import datetime, timedelta


def lastWday():
	now = datetime.now()
	offset = (now.weekday() - 2) % 7
	last_wednesday = now - timedelta(days=offset)
	last_wednesday_str = last_wednesday.strftime('%d-%B-%Y')
	print(last_wednesday_str)
	return (last_wednesday_str)

def nWday():
    now = datetime.now()
    offset = (now.weekday() - 2) % 7
    if offset == 0:
        offset = 7  # if today is Wednesday, we want next week's Wednesday
    next_wednesday = now + timedelta(days=offset)
    next_wednesday_str = next_wednesday.strftime('%d-%B-%Y')
    return next_wednesday_str

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

def hideSheet(spreadsheet,worksheet):
	sheetId = worksheet.id
	spreadsheet.batch_update(body={
	    'requests': [
	        {'updateSheetProperties': {
	            'properties': {
	                'sheetId': sheetId,
	                'hidden': True
	            },
	            'fields': 'hidden'
	        }
	        }
	    ]
	}
	)

def unHideSheet(spreadsheet,worksheet):
	sheetId = worksheet.id
	spreadsheet.batch_update(body={
	    'requests': [
	        {'updateSheetProperties': {
	            'properties': {
	                'sheetId': sheetId,
	                'hidden': False
	            },
	            'fields': 'hidden'
	        }
	        }
	    ]
	}
	)


def lockSheet(spreadsheet,worksheet):
	# print(sh.worksheets())
	emailAddress = "dolphy.phanle@gmail.com" # Please set your email address.
	sheetId = worksheet.id
	body = {
	    "requests": [
	        {
	            "addProtectedRange": {
	                "protectedRange": {
	                    "range": {
	                        "sheetId": sheetId
	                    },
	                    "unprotectedRanges": [
	                        {
	                            "sheetId": sheetId,
	                            "startRowIndex": 0,
	                            "endRowIndex": 1,
	                            "startColumnIndex": 0,
	                            "endColumnIndex": 1
	                        }
	                    ],
	                    "editors": {
	                        "domainUsersCanEdit": False,
	                        "users": [emailAddress]
	                    },
	                    "warningOnly": False
	                }
	            }
	        }
	    ]
	}
	spreadsheet.batch_update(body)

def lockWorksheet(spreadsheet,worksheet):
	# print(sh.worksheets())
	emailAddress = "dolphy.phanle@gmail.com" # Please set your email address.
	sheetId = worksheet.id
	body = {
	    "requests": [
	        {
	            "addProtectedRange": {
	                "protectedRange": {
	                    "range": {
	                        "sheetId": sheetId
	                    },
	                    "unprotectedRanges": [
	                        {
	                            "sheetId": sheetId,
	                            "startRowIndex": 6,
	                            "endRowIndex": 20,
	                            "startColumnIndex": 2,
	                            "endColumnIndex": 3
	                        }
	                    ],
	                    "editors": {
	                        "domainUsersCanEdit": False,
	                        "users": [emailAddress]
	                    },
	                    "warningOnly": False
	                }
	            }
	        }
	    ]
	}
	spreadsheet.batch_update(body)

def createNewSheet(sh):
    worksheet = sh.worksheet("Template")
    new_sheet_name = "Live"
    previous_sheet = lastWday()
    existing_sheets = sh.worksheets()
    # Unhide template sheet
    unHideSheet(sh,worksheet)
    # Check if the "Live" sheet exists
    live_sheet_exists = any(ws.title == new_sheet_name for ws in existing_sheets)
    previous_sheet_exists = any(ws.title == previous_sheet for ws in existing_sheets)

    if live_sheet_exists:
      if not previous_sheet_exists:
        # If "Live" exists but lastWday() sheet doesn't, rename "Live" to lastWday()
        live_sheet = sh.worksheet(new_sheet_name)
        # duplicate live sheet and with new name as last Wednesday.
        lastwed_worksheet = sh.duplicate_sheet(live_sheet.id, new_sheet_name=previous_sheet)
        lockSheet(sh, lastwed_worksheet)
        # hideSheet(sh,lastwed_worksheet)
        # delete the current live sheet
        sh.del_worksheet(live_sheet)
       
        print(f"Renamed 'Live' to '{previous_sheet}'.")
        new_worksheet = sh.duplicate_sheet(worksheet.id, new_sheet_name=new_sheet_name)
        new_worksheet.update('C2', 'Wednesday Football - ' + nextWednesday())
        lockWorksheet(sh, new_worksheet)
        
        print(f"Created new sheet 'Live'.")
      else:
      	print("All done.")
    else:
    	print("3")
    	# new_worksheet = sh.duplicate_sheet(worksheet.id, new_sheet_name=new_sheet_name)
    	# new_worksheet.update('C2', 'Wednesday Football - ' + nextWednesday())
    	# lockWorksheet(sh, new_worksheet)
    hideSheet(sh,worksheet)
    lastwed_worksheet = sh.worksheet(previous_sheet)
    hideSheet(sh,lastwed_worksheet)


if __name__ == "__main__":
	# gc = gspread.service_account()
	gc = gspread.oauth(
	    credentials_filename='~/.config/gspread/credentials.json',
	    authorized_user_filename='~/.config/gspread/authorized_user.json'
	)

	sh = gc.open("1Spatial Football - 2023")

	createNewSheet(sh)
	# print(nextWednesday())
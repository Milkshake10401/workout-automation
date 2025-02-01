import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

# Authenticate with Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("../credentials.json", scope)
client = gspread.authorize(creds)

# Open Google Sheets document
spreadsheet = client.open("Workout Tracker")  # Change this to your actual sheet name
log_sheet = spreadsheet.worksheet("Log Sheet")
weekly_schedule = spreadsheet.worksheet("Weekly Schedule")

# Load data
weekly_data = pd.DataFrame(weekly_schedule.get_all_records())
log_data = pd.DataFrame(log_sheet.get_all_records())

# Merge Data
log_data = log_data.merge(
    weekly_data[['Date', 'Workout Type', 'Exercises Performed']],
    on=['Date', 'Workout Type'],
    how='left'
)

# Update Google Sheets with new data
log_sheet.update([log_data.columns.values.tolist()] + log_data.values.tolist())

print("✅ Workout log updated successfully!")

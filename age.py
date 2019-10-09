from datetime import datetime
def convert(year,month,day):
	dob=datetime(year,month,day)
	age=int((datetime.today()-dob).days/365)
	return age


date_entry = input('Enter a date in YYYY-MM-DD format')
year,month,day = map(int, date_entry.split('-'))

age=convert(year,month,day)
print("years :",age)

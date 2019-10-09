
def convert(number):
	hours=number//60
	mins=number%60
	
	return hours,mins
	
value=int(input("enter the number to be converted"))
hours,mins=convert(value)
print(hours,":",mins)

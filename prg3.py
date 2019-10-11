

str=input("enter the string")

def changeString(str):	
	new_str =""
	new_str2=""
	
	for x in str:
		if(x.isalpha()):
			y=chr(ord(x)+1)
			str=str.replace(x,y)
		
		
	for x in str:
		if(x=="a"or x=="e"or x=="i"or x=="o"or x=="u"):
			y=x.upper()
			new_str2=str.replace(x,y)
	return new_str2
new_str2=changeString(str)
print(new_str2)

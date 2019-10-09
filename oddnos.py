def oddNumbers(num1,num2):
	list1=[]
	
	for x in range(num1,num2):
		if(x%2 != 0):
			list1.append(x)
	return list1
num1,num2=map(int,input("enter the two numbers").split(" "))
print(oddNumbers(num1,num2))
		

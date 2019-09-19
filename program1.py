students = {'1MS17IS001':'Asha','1MS17IS002':'Ashok','1Ms17IS003':'Rekha','1MS17IS004':'suman'}
list =["value1",'value2','value3','value4']
list2=[]
j=0;
for i in students:

	print("key is",i,"Value is",students[i])
	list[j] = students[i]
	j=j+1
print(list)
print(students.keys())
print(students.values())
print(students.items())

#to remove duplicates in a list
list1=[]
n=int(input("enter the number of elements"))
for i in range(0,n):
	ele=input()
	list1.append(ele)
def remove_duplicates(numbers):
	newlist=[]
	for number in numbers:
		if number not in newlist:
			newlist.append(number)
	print(newlist);
	return newlist
remove_duplicates(list1)
	
  
  
  
  
  #to reverse a list
  S =[x**2 for x in range(10)]
print(S)
M=[x for x in S if x%2==0]
M.reverse()
print(M)


#to count the frequency of words in a document
from collections import Counter
def word_count(fname):
	with open(fname) as f:
		return Counter(f.read().split())
print("Number of words in the file:",word_count("test.txt"))

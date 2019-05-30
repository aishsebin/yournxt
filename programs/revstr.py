#problem 2: program to reverse string wrt words

str=input("Enter string: ")
data=str.split(" ")
# print(data)

while '' in data:
    data.remove('')

# print(data)

x=len(data)-1
revstr=data[x]

while(x>0):
    x-=1
    revstr=revstr+" "+data[x]
    
print("Reverse str:",revstr)

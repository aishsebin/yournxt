#problem 2: program to reverse string wrt words


 
# # data=str.split(" ")
# # print(data)

# while '' in data:
#     data.remove('')

# # print(data)

# x=len(data)-1
# revstr=data[x]

# while(x>0):
#     x-=1
#     revstr=revstr+" "+data[x]
    
# print("Reverse str:",revstr)

revstr=""
stack=[]

# global i
i=-1
def push(x):
    global i
    global stack
    # if(i==-1):
    #     i=0
    # else:
    i+=1
  
    stack+=[x]
    
    
def pop():
    global i
    global stack
    x=stack[i]
    stack=stack[:i]
    i-=1
    return x


def isempty():
    global i
    if(i==-1):
        return 1
    else:
        return 0


str=input("Enter string: ")
j=len(str)-1
while(j>=0):
    if(str[j]!=' '):
        push(str[j])
    else:
        if(isempty()==0):
            while(isempty()==0):
                revstr=revstr+pop()
            revstr+=" "
    j-=1 

while(isempty()==0):
    revstr=revstr+pop()
print("Reverse str:",revstr)

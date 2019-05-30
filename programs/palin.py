#problem 1: palindrome

def topal(palin):
    if(len(palin)%2==0):
        if(len(string)%2==0):
            i=len(palin)-1
        else:
            i=len(palin)-2
    else:
        if(len(string)%2==0):
            i=len(palin)-1
        else:
            i=len(palin)-2
    while(i>=0):
        palin=palin+palin[i]
        i-=1
    return palin

string=input("Enter string: ")
try:
    intpal=int(string)
    print(intpal)
except:
    print("Not an integer")
    exit()
x=int(len(string)/2)
if(len(string)%2!=0):
    x+=1

palin=string[:x]
palin=topal(palin)


if(int(palin)>=intpal):
    palin=string[:x]
    palin2=str(int(palin)-1)
    if(len(palin2)<len(palin)):
        if(len(string)%2==0):
            palin2=palin2+palin2[len(palin2)-1]
            palin=palin2
            i=len(palin)-2
            while(i>=0):
                palin=palin+palin[i]
                i-=1
        else:
            palin=palin2
            i=len(palin)-1
            while(i>=0):
                palin=palin+palin[i]
                i-=1
    else:
        palin=topal(palin2)

print(palin)
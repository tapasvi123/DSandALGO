str=input("Enter a String\n")
def check_palindrome(s,e):
    str2=str[s:e]
    if str2==str2[::-1]:
        return True
    else:
        return False
    
def pal():
    s=0
    e=(len(str)-1)
    while(s<e):
        print(str[s])
        if (str[s]!=str[e]):
            if (check_palindrome(s,e))  or (check_palindrome(s+1,e+1)):
                return True
            else:
                return False
        s+=1
        e-=1
    return True
    
print(pal())
    
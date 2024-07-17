import re


def charactercheck(passwd):
    s,n,u=0,0,0
    l=len(passwd)
    for i in passwd:
        if i.isalpha() and i.isupper():
            u+=1
        elif i.isdigit():
            n+=1
        elif not(i.isalnum()):
            s+=1
    return s,n,u

def pass_complexity(passwd):
    s,n,u =charactercheck(passwd)
    pass_complex=min(s, 10)+min(len(passwd), 10)+ min(n, 10)+min(u, 10)

    complex_percentage=(pass_complex/40)*100
    rest=100-complex_percentage
    complexstr="#"*int(int(complex_percentage)/2)+("_"*int(int(rest)/2))
    print(f"\n[{complexstr}] {complex_percentage}\n\nAnalysing password....\n\nLength: {len(passwd)}\n\nSpecial Character: {s}\n\nDigits: {n}\n\nUppercase character: {u}\n\n") 

    


print("\n\n------TEST YOUR PASSWORD COMPLEXITY------\n\n The password should be more than 8 characters, include\n specialcharacters numbers, upper case letters,etc..")

passwd=""

while len(passwd)<=8:

    passwd=input("\nEnter your password: ")
    special, digits, upper=charactercheck(passwd)

    if len(passwd)<8:
        print("Re-Enter the password!..\n")
        continue
    else:
        if special==0:
            print("Yoru password should contains atleast 1 special character!..")
        elif digits==0:
            print("your password should contains atleast 1 digit!..")
        elif upper==0:
            print("Your password should contain atleast 1 UPPERCASE character!..")    
        else:
            pass_complexity(passwd)

        



            
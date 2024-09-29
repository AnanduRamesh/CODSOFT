#Password generartor
import string
import random
def password(len):
    low = string.ascii_lowercase
    dig = string.digits
    punc = string.punctuation
    up = string.ascii_uppercase
    chars = low+dig+punc+up
   #char='abcdfghijklmnopqrstuvwxyxABCDEFGHIJKLNOPQRSTUVWXYZ1234567890~!@#$%^&*()'
    pswd=[]
    for _ in range(len):
        pswd.append(random.choice(chars))
    
    password = ''.join(pswd)
    return password

def main():
    try:
        l = int(input("Enter length for password:"))
        if l<8:
            print("Password should contain atleast 8 characters")
        else:
            pswd = password(l)
            print(f"Password generated is : {pswd}")
    except ValueError:
        print("Invalid")
if __name__=="__main__":
    main()

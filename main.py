import string
import random

if __name__ == "__main__":
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    #print(s)
    random.shuffle(s)
    #print(s)

    check = True
    while check == True:
        plen = input("enter the length of the password: ")
        if plen.isdigit() == True:
            p_length = int(plen)
            check = False
        else:
            print("enter a valid integer")
            continue

    password = "".join(s[0:p_length])

    print(password)

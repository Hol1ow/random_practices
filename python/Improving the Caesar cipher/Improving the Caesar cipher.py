inp = input("Enter a string: ")
salt = ""
while True:
    salt = input("Enter salt value: ")
    if salt.isdigit():
        salt = int(salt)
        if 0 < salt < 26:
            break
    print("Invalid, try again")
  
res = ""  
for c in inp:
    if c.isalpha():
        if c.isupper():
            c = ord(c) + salt
            while c > ord('Z'):
                c = c - ord('Z') + ord('A') - 1
            res += chr(c)
        else:
            c = ord(c) + salt
            while c > ord('z'):
                c = c - ord('z') + ord('a') - 1
            res += chr(c)
    else:
        res += c
        
print(res)

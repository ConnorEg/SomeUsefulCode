def encrypt(key, n, plaintext):
    cipher=[]
    m=0
    for i in plaintext:
        m=ord(i)
        c=(m**key)%n
        cipher.append(c)
    cipher = str(cipher)
    cipher = cipher[1:-1]
    return cipher

message = input("Enter a message to encrypt: ")
pubkey = int(input("Enter the public key of other person: "))
mod = int(input("Enter the mod: "))

x=encrypt(pubkey, mod, message)
print ("Encrypted message: ")
print (x)

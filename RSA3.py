def decrypt(key, n, ciphertext):
    key = int(key.strip())
    n = int(n.strip())
    
    txt=ciphertext.split(',')
    msg=''
    m=0
    for i in txt:
        m=(int(i)**key)%n
        msg += chr(m)
    return msg

f=open("keys.txt", "r")
k = f.readlines()
cipher = input("Enter a message to decrypt in comma separated values: ")

print ("Decrypting message with private key")
print (decrypt(k[0], k[1], cipher))

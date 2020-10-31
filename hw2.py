#determines if the number entered is prime
def isPrime(n):
    if n > 1:
        for i in range(2,n):
            if(n%i == 0):
                return 0
    else:
        return 0
    return 1

#changes the plainText to numbers 0-27
def textToNum():
    for element in range(0, len(plainText)):
        number = 0
        text = ""
        if plainText[element] >= 'a' and plainText[element] <= 'z':
            number = ord(plainText[element]) - 96
        elif plainText[element] == ' ':
            number = 27
        else:
            text += "0"
        if number < 10:
            text += "0"
        text += str(number)
        numText.append(text)

#returns the gcd of phi and n
def gcd(phi, n):
    while(n):
        phi,n = n,phi%n
    return phi

#encrypts the message using the public key 
def encryptmessage():
    for i in numText:
        x = (int(i) ** e) % n # m^e mode n 
        cipherText.append(x)


#decrypts ciphertext using the private key 
def decryptmessage():
    decryptText = ""
    for i in cipherText:
        x = (i ** d) % n # c^d mod n
        if x == 27:
            decryptText += chr(32)
        else:
            decryptText += chr(x+96)
    return decryptText

#Start of program
p=0
q=0
runtime = 0
#continues while p and q aren't prime
while runtime < 1:
    p = input("Enter p: ")
    p = int(p)
    q = input("Enter q: ")
    q =int(q)
    runtime = isPrime(p)
    if runtime == 1:
        runtime = isPrime(q)
    #check if p and q are prime
    if runtime < 1:
        print("p and/or q are not prime. Try again!")
    else:
        #n must be greater than one block of max value 27
        if( p*q <= 27 ):
            print("Please pick different p and/or q values")
            runtime = 0
        else:
            runtime = 1

#calculate e
e = 0
phi = (p-1)*(q-1)
for i in range(2, phi):
    value = gcd(phi, i)
    if(value == 1):
        e = i
        break

#calculate d
d = 0
for i in range(2, phi):
    value = (i * e) % phi
    if(value == 1 and e != i):
        d = i
        break

#display the public and private key
n = p*q
print("Public key is (e,n): (" + str(e) + "," + str(n) + ")")
#print("(",e,",",n,")")
print("Private key is d: " + str(d))
#print(d)

#get plainText and change to numbers 0-27
numText = [] 
while runtime > 0:
    plainText = input("Enter plaintext (Only lowercase a->z is accepted as well as SPACE): ")
    textToNum()
    if len(numText) != 0:
        runtime = 0
    if runtime > 0:
        print("Please enter a some text. Try again!")

#encrypt plainText to cipherText using block size 1 char
cipherText = []
encryptmessage()

#decrypt cipherText to decryptText
decryptText = decryptmessage()

#print both output of encyption and decyption methods 
print("Cipher Text: " + str(cipherText))
print("Plain Text: " + decryptText)





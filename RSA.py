import math

def isPrime(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True 

def phi(p, q):
    return (p-1) * (q-1)

def generateD(e, n):
    i = 0
    while (e * i) % n != 1:
        i += 1
    return i

def encrypt(string, e, n):
    alphabets = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}
    num = ""
    for letter in string:
        num += str(alphabets[letter])
    num = int(num)
    return (num**e) % n

def decrypt(num, d, n):
    num = (num**d) % n
    return num

if __name__ == "__main__":
    prime1 = int(input("Enter your Fisrt Prime Number: "))
    while not isPrime(prime1):
        print("Not a Prime Number.")
        prime1 = int(input("Enter again: "))
    
    prime2 = int(input("Enter your Second Prime Number: "))
    while not isPrime(prime2):
        print("Not a Prime Number.")
        prime2 = int(input("Enter again: "))
    
    n = prime1 * prime2
    phiN = phi(prime1, prime2)

    e = int(input(f"Enter value of e which is a relative Prime of {phiN} and 1 < e < {phiN}: "))
    while math.gcd(e, phiN) != 1 or e < 0:
        e = int(input("Enter again: "))
    
    d = generateD(e, phiN)

    print(f"\nPublic Key is:{{{e},{n}}}")
    print(f"Private Key is:{{{d},{n}}}")
    message = input("\nEnter the message: ").upper()
    message = message.replace(" ","")

    msg_encrypt = encrypt(message, e, n)
    print("\nMessage after Encryption:",msg_encrypt)

    msg_decrypt = decrypt(msg_encrypt, d, n)
    print("Message after Decryption:",msg_decrypt)
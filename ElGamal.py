import random

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

def isPrimitive(root, q):
    if q < root:
        return False
    else:
        values = []
        for i in range(q-1):
            mod = root**(i+1) % q
            if mod >= q:
                return False
            else:
                values.append(mod)
        if len(set(values)) == len(values):
            return True
        else:
            return False

def encrypt(M, root, Ya, q):
    k = random.randint(1, q-1)
    K = (Ya**k) % q
    C1 = (root**k) % q
    C2 = (K*M) % q
    return C1, C2

def decrypt(C1, C2, Xa, q):
    K = (C1**Xa) % q
    i = 0
    while (K * i) % q != 1:
        i += 1
    return (C2*i) % q

if __name__ == '__main__':
    q = int(input('\nEnter the value of Prime number "q": '))
    while not isPrime(q):
        print("Not a Prime Number.")
        q = int(input("Enter again: "))
    
    root = int(input('Enter the Primitive root of "q": '))
    while not isPrimitive(root, q):
        print('Not a Primitive Root OR value is greater than "q"')
        root = int(input('Enter Again: '))
    
    Xa = random.randint(2, q-2)
    Ya = (root**Xa) % q

    print(f"\nPublic Key is:{{{q},{root},{Ya}}}")
    print(f"Private Key is:{{{Xa}}}")

    M = int(input('\nEnter Message: '))
    while M >= q or M < 0:
        print(f'Error!! Choose between 0 and {q-1}')
        M = int(input('Enter Again: '))

    C1, C2 = encrypt(M, root, Ya, q)
    print("\nAfter Encryption.")
    print(f'C1 is: {C1}')
    print(f'C2 is: {C2}')
    
    msg = decrypt(C1, C2, Xa, q)
    print('\nAfter Decryption.')
    print(f'Message is: {msg}')
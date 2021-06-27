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

def generatePublicKey(pvt_key, root, q):
    return (root**pvt_key) % q

def generateSecretKey(pbl_key, pvt_key, q):
    return (pbl_key**pvt_key) % q


if __name__ == '__main__':
    q = int(input('Enter the value of Prime number "q": '))
    while not isPrime(q):
        print("Not a Prime Number.")
        q = int(input("Enter again: "))
    
    root = int(input('Enter the Primitive root of "q": '))
    while not isPrimitive(root, q):
        print('Not a Primitive Root OR value is greater than "q"')
        root = int(input('Enter Again:'))
    
    pvt_keyA = int(input('Enter the Private Key of user A: '))
    while pvt_keyA > q or pvt_keyA <= 0:
        print(f'Error!! Choose between 0 and {q}')
        pvt_keyA = int(input('Enter Again: '))
    pbl_keyA = generatePublicKey(pvt_keyA, root, q)
    
    pvt_keyB = int(input('Enter the Private Key of user B: '))
    while pvt_keyB > q or pvt_keyB <= 0:
        print(f'Error!! Choose between 0 and {q}')
        pvt_keyB = int(input('Enter Again: '))
    pbl_keyB = generatePublicKey(pvt_keyB, root, q)

    sec_keyA = generateSecretKey(pbl_keyB, pvt_keyA, q)
    print(f'\nSecret key of user A is: {sec_keyA}')

    sec_keyB = generateSecretKey(pbl_keyA, pvt_keyB, q)
    print(f'Secret key of user B is: {sec_keyB}')
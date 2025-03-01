import time
alphabet = 'abcdefghijklmnopqrstuvwxyz'
final = ''
def Ceasar (message, key):
    for i in message: 
        global final
        n=alphabet.find(i)
        m= n+key
        if m >= len(alphabet):
            key = m - len(alphabet)-n
            m= n+key
        if i in alphabet:
            final+=alphabet[m]
        else:
            final += i
message=str(input())
key=int(input())
Ceasar (message,key)
print(final)
time.sleep(5)  
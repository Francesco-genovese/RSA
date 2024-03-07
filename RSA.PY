from ast import literal_eval
import random 
import Crypto.Util.number
import math  
import time
import sys


def data():
    m = input('vuoi creare il file? ')
    if m == 'si':
        f  = open('RSA.txt', 'w')
        f.write('lunghezza primary: '+ str(N) + '\n')
        f.write('numero primari p: '+ str(p) + '\n')
        f.write('secondary primari q: '+ str(q) + '\n')
        f.write('il tuo testo criptato:  '+ str(compC) + '\n')
        f.write('la tua chiave per decriptare: '+ str(d) + '\n')
        f.write('il tuo testo decriptato(se lo hai richiesto): '+ str(compD) + '\n')
        f.write('il tempo di esecuzione di questo per criptare: ' + str(tempoC) + ' sec\n')
        f.write('il tempo di esecuzione di questo per decriptare: ' + str(tempoD) + ' sec\n')
        f.close()
    ss = input("vuoi avaere i dati a schermo ? ")
    if ss == "si" or ss=="SI":
        print("tempo di crittazione: " + str(tempoC)+' sec\n')
        print("tempo decrittazione: "+ str(tempoD)+ ' sec\n')
        print("la tua chiave per decriptare è : "+ str(d) + '\n')
    else: 
            print('arrivederci')

scelta  = input ("cosa vuoi fare ? criptare o decriptare ? (c/d): ")

if(scelta == "c" or scelta == "C"):
    print("""RSA CODER""")

    text = input("inserisci la frase da criptare: ")
    ascii_values = [ord(character) for character in text]
    print('')

    startC = time.time()
    N=10
    q= Crypto.Util.number.getPrime(N, randfunc=None)
    f=1
    while(f!=0):
        p = Crypto.Util.number.getPrime(N, randfunc=None)
        if(q!=p):
            f=0
    p = int(p)
    q = int(q)
    e=0
    d=0            
    n = p*q 
    phi=(p-1)*(q-1)
    a = 1
    while(a!=0):
        e = random.randint(1,(phi-1))
        MCD=math.gcd(phi, e)
        if MCD == 1: 
            a = 0
        else: 
            a = 1
    ArrC = []
    for i in ascii_values:
        c = pow(int(i),int(e),int(n))
        ArrC.append(hex(c))
    compC=''.join(ArrC)
    print(compC)
    endC = time.time()
    startD = time.time()
    d = pow(int(e), -1, int(phi))
    tempoC = (endC - startC)
    compD = 0
    tempoD = 0
    data() 


elif (scelta == "d" or scelta == "D" ):
    #decripter
    time.sleep(1)
    print('')
    print('')
    print('')
    print("""RSA DECODER""")
    ArrD = []
    ArrC = input('inserisci la frase da deciptare: ')
    p = input( 'inserisci la tua p: ')
    q = input( 'inserisci la tua q: ')
    n = int(p)*int(q)
    d = input ('inserrisci la key: ')
    startD = time.time()
    for i in ArrC.split('0x')[1:]:
        m = pow(int(i, 16), int(d), int(n))
        ArrD.append(chr(m))
    compD=''.join(ArrD)
    print(compD)
    endD = time.time()
    tempoD = (endD - startD)
    compC = 0
    tempoC = 0
    N = 0
    data()
else:
    print("scelta nn valida")
    exit 




#R3tr0 
#V. 9.0
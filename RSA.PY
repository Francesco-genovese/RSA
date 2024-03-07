from ast import literal_eval
import random 
import Crypto.Util.number
import math  
import time
import os 

def file():
    while True:
        file_path = input("Inserisci il percorso completo del file di testo: ")
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                content_array = file.readlines()
            print("Contenuto del file memorizzato nell'array:")
            for line in content_array:
                print(line.strip()) 
            return content_array
            break
        else:
            print("Il file specificato non esiste.")
            
def data():
    m = input('vuoi creare il file? ')
    if m == 'si':
        f  = open('Outout.txt', 'w')
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

while True:
    scelta  = input ("cosa vuoi fare ? criptare o decriptare ? (c/d): ")

    if(scelta == "c" or scelta == "C"):
        print("""RSA CODER""")
        while True:
            ds = input ("come vuoi criptare? da file o scrivere un testo ? (f / t): ")
            if ds == "f":
                text = file()
                ascii_values = [ord(character) for line in text for character in line.strip()]
                break
            elif ds == "t":
                text = input("inserisci la frase da criptare: ")
                ascii_values = [ord(character) for character in text]
                break
            else: 
                print (" scelta nn valida")
            
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
        for line in text:
            for char in line.strip():
                c = pow(ord(char), int(e), int(n))
                ArrC.append(hex(c))
        compC = ' '.join(ArrC) 
        print('il testo criptato : ' + compC)
        f = open('inputfile.txt', 'w')
        f.write(str(compC))
        f.close()
        endC = time.time()
        startD = time.time()
        d = pow(int(e), -1, int(phi))
        tempoC = (endC - startC)
        compD = 0
        tempoD = 0
        data() 
        break
    elif (scelta == "d" or scelta == "D" ):
        #decripter
        print('')
        print("""RSA DECODER""")
        ArrD = []
        
        p = input( 'inserisci la tua p: ')
        q = input( 'inserisci la tua q: ')
        n = int(p)*int(q)
        d = input ('inserrisci la key: ')
        
        while True:
            ds = input ("come vuoi decriptare? da file o scrivere un testo ? (f / t): ")
            if ds == "f":
                startD = time.time()
                ArrC = file()
                for line in ArrC:
                    hex_values = line.split('0x')[1:]
                    for hex_value in hex_values:
                        m = pow(int(hex_value, 16), int(d), int(n))
                        ArrD.append(chr(m))
                break
            elif ds == "t":
                startD = time.time()
                ArrC = input('inserisci la frase da decifrare: ')
                for i in ArrC.split('0x')[1:]:
                    m = pow(int(i, 16), int(d), int(n))
                    ArrD.append(chr(m))
                break
            else: 
                print("scelta nn valida")       
        compD=''.join(ArrD)
        print('il testo decriptato è: '+ compD)
        endD = time.time()
        tempoD = (endD - startD)
        compC = 0
        tempoC = 0
        N = 0
        data()
        break
    else:
        print("scelta nn valida")




#R3tr0 
#V. 10.0
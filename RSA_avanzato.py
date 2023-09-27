from ast import literal_eval
import random 
import Crypto.Util.number
import math  
import time
import sys
sys.set_int_max_str_digits(100000)

print("""\
 ██▀███    ██████  ▄▄▄          ▄████▄   ▒█████  ▓█████▄ ▓█████  ██▀███  
▓██ ▒ ██▒▒██    ▒ ▒████▄       ▒██▀ ▀█  ▒██▒  ██▒▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒
▓██ ░▄█ ▒░ ▓██▄   ▒██  ▀█▄     ▒▓█    ▄ ▒██░  ██▒░██   █▌▒███   ▓██ ░▄█ ▒
▒██▀▀█▄    ▒   ██▒░██▄▄▄▄██    ▒▓▓▄ ▄██▒▒██   ██░░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄  
░██▓ ▒██▒▒██████▒▒ ▓█   ▓██▒   ▒ ▓███▀ ░░ ████▓▒░░▒████▓ ░▒████▒░██▓ ▒██▒
░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░   ░ ░▒ ▒  ░░ ▒░▒░▒░  ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░▒ ░ ▒░░ ░▒  ░ ░  ▒   ▒▒ ░     ░  ▒     ░ ▒ ▒░  ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░
  ░░   ░ ░  ░  ░    ░   ▒      ░        ░ ░ ░ ▒   ░ ░  ░    ░     ░░   ░ 
   ░           ░        ░  ░   ░ ░          ░ ░     ░       ░  ░   ░     
                               ░                  ░                      
""")

text = input("ｉｎｓｅｒｉｓｃｉ ｌａ ｆｒａｓｅ ｄｉ ｃｒｉｐｔａｒｅ： ")
ascii_values = [ord(character) for character in text]
print('')

startC = time.time()
N=8192 
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
print(ArrC)
endC = time.time()
startD = time.time()
d = pow(int(e), -1, int(phi))

#decripter
time.sleep(3)
print('')
print('')
print('')
print("""\
 ██▀███    ██████  ▄▄▄         ▓█████▄ ▓█████  ▄████▄   ▒█████  ▓█████▄ ▓█████  ██▀███  
▓██ ▒ ██▒▒██    ▒ ▒████▄       ▒██▀ ██▌▓█   ▀ ▒██▀ ▀█  ▒██▒  ██▒▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒
▓██ ░▄█ ▒░ ▓██▄   ▒██  ▀█▄     ░██   █▌▒███   ▒▓█    ▄ ▒██░  ██▒░██   █▌▒███   ▓██ ░▄█ ▒
▒██▀▀█▄    ▒   ██▒░██▄▄▄▄██    ░▓█▄   ▌▒▓█  ▄ ▒▓▓▄ ▄██▒▒██   ██░░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄  
░██▓ ▒██▒▒██████▒▒ ▓█   ▓██▒   ░▒████▓ ░▒████▒▒ ▓███▀ ░░ ████▓▒░░▒████▓ ░▒████▒░██▓ ▒██▒
░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░    ▒▒▓  ▒ ░░ ▒░ ░░ ░▒ ▒  ░░ ▒░▒░▒░  ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░▒ ░ ▒░░ ░▒  ░ ░  ▒   ▒▒ ░    ░ ▒  ▒  ░ ░  ░  ░  ▒     ░ ▒ ▒░  ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░
  ░░   ░ ░  ░  ░    ░   ▒       ░ ░  ░    ░   ░        ░ ░ ░ ▒   ░ ░  ░    ░     ░░   ░ 
   ░           ░        ░  ░      ░       ░  ░░ ░          ░ ░     ░       ░  ░   ░     
                                ░             ░                  ░                      
""")
ArrD = []
r = input('ｖｕｏｉ ｄｅｃｒｉｐｔａｒｅ ？ ')
if r=='si' or r=='SI':
    startD = time.time()
    for i in ArrC:
        m = pow(literal_eval(i),int(d),int(n))
        ArrD.append((chr(m)))
    print(ArrD)
    endD = time.time()
else:
    print('ａｒｒｉｖｅｄｅｒｃｉ')


tempoC = (endC - startC)
tempoD = (endD - startD)
f  = open('RSA.txt', 'w')
f.write('lunghezza primary: '+ str(N) + '\n')
f.write('numero primari p: '+ str(p) + '\n')
f.write('secondary primari q: '+ str(q) + '\n')
f.write('il tuo testo criptato:  '+ str(ArrC) + '\n')
f.write('la tua chiave per decriptare: '+ str(d) + '\n')
f.write('il tuo testo decriptato(se lo hai richiesto): '+ str(ArrD) + '\n')
f.write('il tempo di esecuzione di questo per criptare: ' + str(tempoC) + ' sec\n')
f.write('il tempo di esecuzione di questo per decriptare: ' + str(tempoD) + ' sec\n')
f.close()


ss = input("vuoi avaere i dati qui a schermo ? ")
if ss == "si" or ss=="SI":
    print("tempo di crittazione: " + str(tempoC)+' sec\n')
    print("tempo decrittazione: "+ str(tempoD)+ ' sec\n')
    print("la tua chiave per decriptare è : "+ str(d) + '\n')
else: 
        print('ａｒｒｉｖｅｄｅｒｃｉ')



#francesco genovese aka -R3tr0 

#V. 7.1 possibilita di viionari e dati a schermo e non solo tramite il file 
#problema del limite dell string risolto.
